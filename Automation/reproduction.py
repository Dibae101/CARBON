import sys
from datetime import datetime
from collections import defaultdict
import uiautomator2 as u2
from hierarchy import *
from execution import *
from my_gpt import *
from utils import *
from bug_validation import *
from handle_command import *
from ui_viewer import capture_viewer_state, clean_screenshots, is_vision_available, build_color_diff

def get_prompt(device, attribute_to_element_map, package_name, execution_status, flags, step_number=0, prev_color_report=None):
    bug_report, need_hint, is_not_completet, repeating_commands = flags
    # first screenshot capture
    widget_dict_1, info_1 = get_screen_information(device, attribute_to_element_map, package_name)
    time.sleep(2) # 2 seconds gap of screenshot before prompt
   # Second  screenshot capture
    attribute_to_element_map_2 = defaultdict(list)
    widget_dict_2, info_2 = get_screen_information(device, attribute_to_element_map_2, package_name)
    
    # Capture UIAutomator Viewer state: annotated screenshot with bounding boxes + element map
    viewer_state = capture_viewer_state(device, step_number=step_number)
    annotated_screenshot = viewer_state.get('annotated', None)
    viewer_legend = viewer_state.get('legend', '')
    color_report = viewer_state.get('color_report', '')
 
    if widget_dict_1 == widget_dict_2:
        info = info_2
        attribute_to_element_map = attribute_to_element_map_2
    else:
        info = f"There are a UI quickly disappear(less than 0.5s) after {execution_status}. The UI information of the page is {{info_1}}. If the next action related to the quick diappear page, Please provide a seris of actions to tigger the quick disappear UI then execute actions on the relevant transient widget in one go. Current page is {info_2}.  It the quick diappear UI is not related, we can ignore it and proceeed based on the state of current page"
    if need_hint:
        hint = "Your suggestion is None. Let's go back or restart"
        prompt = f"{hint}. {info}"
        flags[1] = False
    elif is_not_completet:
        hint = 'Has not trigger a bug yet'
        prompt = f"{hint}. {info}"
        flags[2] = False
    elif repeating_commands:
        warning = f"Just a reminder, we are repeating the following steps {repeating_commands}. If the bug report doesn' require repeated steps, it seems like we're trapped into a loop. If you belive we are in the right track, maybe try different text for set_text. If there are more other widgets, maybe try a different path"
        prompt =  prompt = f"{warning}. {info}"
        flags[3] = None
    else:
     
        prompt = f"{execution_status}.{info}"

    # Append UIAutomator Viewer element map to prompt for cross-referencing with annotated screenshot
    if viewer_legend:
        prompt = f"{prompt}\n\n{viewer_legend}"

    # Append color analysis so Gemini can compare colors across steps
    if color_report:
        prompt = f"{prompt}\n\n{color_report}"

    # Append explicit color diff vs previous step (saves Gemini from searching history)
    color_diff = build_color_diff(prev_color_report, color_report)
    if color_diff:
        prompt = f"{prompt}\n\n{color_diff}"
   
    return widget_dict_2, prompt, annotated_screenshot, color_report

def execute_commands(command_list, device, widget_dict, attribute_to_element_map, package_name):
    if command_list is  None:
        return "No sugggestion"
    execution_status = []
    for command in  command_list:  
        try:
            status = handle_command(command, device, attribute_to_element_map, package_name)
            if status == True :
                if command['action'] in ['swipe']:
                    execution_status.append(f"Successfully execute {command} but please make sure you swipe to the correct location, if not either keep swiping or change the from_direction and to_direction. And keep in mind that swiping betwwen multi-page layout, one swipe is just going to the next layout ")
                else:
                    execution_status.append(f"Successfully execute {command}")
            
            elif status == False:
                execution_status.append(f"Failed to execute {command}")
            else:
                execution_status.append(status)
        except Exception as e:
            execution_status.append(f"Failed to execute {command}. Error message: {e}")

        # Skip inter-step delay for quick_tap — the whole point is minimal latency
        if command.get('action') != 'quick_tap':
            time.sleep(0.5)
    return execution_status

def reproduce_bug(device_port, reprot_file_name): 
   
    device = u2.connect(f"emulator-{device_port}")
    clear_logcat(device_port)

    device.set_orientation("natural")
    package_name = device.app_current()['package']
    bug_report = read_bug_report(reprot_file_name)

    history = load_training_prompts('./prompts/training_prompts_ori.json')
    
    # Clean previous screenshots for fresh run
    clean_screenshots()
    if is_vision_available():
        print("[UIAutomator Viewer] ENABLED - annotated screenshots with color-coded bounding boxes will be sent to Gemini")
    else:
        print("[UIAutomator Viewer] DISABLED - install Pillow to enable: pip install Pillow")

  
    
    #print(br_content)
    #history.append({"role": "user", "content": br_content})
    history.append({"role": "user", "content": f"{bug_report}"})
    execution_data = [datetime.now(), 0, 0] # current time, num response, num commands
    flags = [None, False, False, None] # bug_report, need_hint, is_not_completet, repeating_commands
    crash = False
    widget_dict, other_text, prompt = None, None, None
    executed_commands, execution_status = [], []
    step_number = 0
    prev_color_report = None  # track colors from previous step for diff
    
    # here the variabel name should be bug_triggered
    while not crash:
        attribute_to_element_map = defaultdict(list) # for current page 
        widget_dict, prompt, screenshot, color_report = get_prompt(device, attribute_to_element_map, package_name, execution_status, flags, step_number=step_number, prev_color_report=prev_color_report)
        prev_color_report = color_report  # store for next iteration's diff
        step_number += 1
        
        print(f"*Prompt: {prompt}") 
        response,  history = generate_text(prompt, history, package_name, screenshot=screenshot)
        message = get_message(response)
        print(get_model_name(response))
        print('###############################################\n')
        print(f"*GPT message: {message}")
        print('\n###############################################')

        command_list = convert_message_to_command_list(message)
        count_command_and_response(execution_data, command_list)
        history.append({"role": "assistant", "content": message})  
        
        if command_list == []:
            flags[1] = True
            device.set_orientation("natural")
            time.sleep(2)
        elif command_list and isinstance(command_list[0], dict) and command_list[0].get('result', None) is not None:
            #if command_list[0].get('result') == 'success':
            if command_list[0].get('result'):
                crash = True # here the variabel name should be bug_triggered
            else:
                flags[1] = True
        elif command_list and isinstance(command_list[0], dict) and command_list[0].get('action', '') == 'check crash':
            crash = check_crash(reprot_file_name, history, package_name, device_port, execution_data)
            if not crash:
                time.sleep(1)
                crash = check_error_keywords(get_current_hierarchy(device), package_name) \
                        or 'crashreport' in device.app_current()['activity'].lower()
                if not crash:
                    flags[2] = True   
        else:
            clear_logcat(device_port)  # fresh slate — only catch exceptions from THIS step
            execution_status = execute_commands(command_list, device, widget_dict, attribute_to_element_map, package_name)
            flags[3] = add_commands(executed_commands, command_list)

            # Logcat Exception Monitor: detect silent failures after command execution
            exc_found, exc_lines = check_logcat_exceptions(device_port, package_name)
            if exc_found:
                exc_report = f"[Logcat Exception Monitor] Detected {len(exc_lines)} exception(s) in app log after executing commands:"
                for eline in exc_lines[:5]:
                    exc_report += f"\n  >> {eline}"
                execution_status.append(exc_report)
                print(exc_report)
        #if not crash:
        #    crash = check_crash(reprot_file_name, history, package_name, device_port, execution_data)
    start_time, response_time, total_commands = execution_data
    log_and_save_history(reprot_file_name, start_time, response_time, total_commands, history, package_name, 'xxx')
    device.set_orientation("natural")
    


def main(device_port, reprot_file_name):
    reproduce_bug(device_port, reprot_file_name)

if __name__ == "__main__":
    if len(sys.argv) == 2: 
        print_screen_information_testing(f"emulator-{sys.argv[1]}")
    elif len(sys.argv) == 3:
        main(sys.argv[1] , sys.argv[2]) #device_id, reprot_file_name
    else:
        print("Usage: python3 script.py <device_port> <file_name>")

    