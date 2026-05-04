"""
Multi-provider LLM client for ReBL.
Reads LLM_PROVIDER, LLM_API_KEY, LLM_MODEL from .env via llm_config.py.
Supports: Gemini, OpenAI, Groq, Ollama, or any OpenAI-compatible endpoint.
"""

import datetime
import math
import time
import json
import os
from utils import *
from llm_config import get_config, rotate_key, get_current_key_info

# Load LLM config
LLM = get_config()
print(f"[LLM] Provider: {LLM['provider']} | Model: {LLM['model']} | Vision: {LLM['supports_vision']}")
print(f"[LLM] Using {get_current_key_info()}")

# ── Provider-specific setup ──────────────────────────────────────────────────

if LLM['type'] == 'gemini':
    import google.generativeai as genai
    genai.configure(api_key=LLM['api_key'])
elif LLM['type'] == 'openai':
    from openai import OpenAI
    _client = OpenAI(api_key=LLM['api_key'], base_url=LLM.get('base_url'))
elif LLM['type'] == 'vertex':
    import requests as _requests

# Check if vision/screenshot support is available
try:
    from ui_viewer import is_vision_available
    VISION_ENABLED = is_vision_available() and LLM['supports_vision']
except ImportError:
    VISION_ENABLED = False


# ── Token counting ───────────────────────────────────────────────────────────

def count_tokens(message):
    return len(message) // 4

def count_chat_history_tokens(chat_history):
    total = 0
    for msg in chat_history:
        total += count_tokens(msg['content'])
        total += count_tokens(msg['role'])
    return total

def truncate_message(message, n):
    estimated = len(message) // 4
    if estimated <= n:
        return False, None
    char_limit = math.floor(n * 4)
    return True, message[:char_limit]


# ── History management ───────────────────────────────────────────────────────

def convert_history_to_text(history):
    text = ""
    for msg in history:
        role = msg['role']
        content = msg['content']
        if role == 'system':
            text += f"System: {content}\n\n"
        elif role == 'user':
            text += f"User: {content}\n\n"
        elif role == 'assistant':
            text += f"Assistant: {content}\n\n"
    return text

def _summarize(history):
    """Summarize history when it gets too long."""
    summary_prompt = ('The conversation is about to exceed the limit, before we '
                      'continue the reproduction process. Can you summarize the '
                      'above conversation. Note that You shouldn\'t summarize the '
                      'rule and keep the rules as original since the rules are the standards.')
    history.append({"role": "user", "content": summary_prompt})

    if LLM['type'] == 'gemini':
        model = genai.GenerativeModel(f"models/{LLM['model']}")
        response = model.generate_content(convert_history_to_text(history))
        return response.text
    elif LLM['type'] == 'vertex':
        result, _ = _generate_vertex(history, LLM['model'], None)
        return result["choices"][0]["message"]["content"]
    else:
        response = _client.chat.completions.create(
            model=LLM['model'],
            messages=history,
            temperature=0.3,
        )
        return response.choices[0].message.content


def process_history(prompt, history, max_tokens, threshold):
    tokens = count_chat_history_tokens(history)

    if tokens > math.floor(max_tokens * threshold):
        last_prompt = history[-1]['content']
        if count_tokens(last_prompt) > 4000:
            del history[-1]
            _, truncated = truncate_message(last_prompt,
                (max_tokens - count_chat_history_tokens(history)) * threshold)
            history.append({"role": "user", "content": truncated})

        print('summarize==========================================')
        message = _summarize(history)
        print(message)
        history = load_training_prompts('./prompts/training_prompts_ori.json')
        history.append({"role": "user", "content": message})

    history.append({"role": "user", "content": prompt})
    return history


# ── Main generate function ───────────────────────────────────────────────────

def generate_text(prompt, history, package_name=None, model_name=None,
                  max_tokens=None, attempts=10, screenshot=None):
    model_name = model_name or LLM['model']
    max_tokens = max_tokens or LLM['max_tokens']

    history = process_history(prompt, history, max_tokens, threshold=0.75)

    for times in range(attempts):
        try:
            if LLM['type'] == 'gemini':
                return _generate_gemini(history, model_name, screenshot)
            elif LLM['type'] == 'vertex':
                return _generate_vertex(history, model_name, screenshot)
            else:
                return _generate_openai(history, model_name, screenshot)

        except Exception as e:
            error_str = str(e).lower()
            print(f"Attempt {times + 1} failed with error: {str(e)}")

            is_quota = ("429" in str(e) or "rate" in error_str or
                        "quota" in error_str or "resource exhausted" in error_str)

            if is_quota:
                # Try rotating to next API key before waiting
                if rotate_key():
                    LLM.update(get_config())
                    print(f"[LLM] Rotated to {get_current_key_info()}, retrying immediately...")
                    continue  # retry immediately with new key
                else:
                    wait_time = min(60 * (2 ** times), 300)
                    print(f"Rate limit hit, no more keys to rotate. Waiting {wait_time}s ({times+1}/{attempts})...")
                    if package_name:
                        save_chat_history(history, package_name)
                    time.sleep(wait_time)
            else:
                if times < attempts - 1:
                    if package_name:
                        save_chat_history(history, package_name)
                    wait = 60 * (times + 1)
                    print(f"Retrying in {wait}s...")
                    time.sleep(wait)
                else:
                    print(f"All {attempts} attempts failed.")
                    if package_name:
                        save_chat_history(history, package_name)
                    raise e


def _generate_gemini(history, model_name, screenshot):
    """Generate using Google Gemini native API."""
    model = genai.GenerativeModel(f"models/{model_name}" if not model_name.startswith("models/") else model_name)
    chat_text = convert_history_to_text(history)

    content_parts = [chat_text]
    if screenshot is not None and VISION_ENABLED:
        content_parts.append(screenshot)
        print("[UIAutomator Viewer] Annotated screenshot included in prompt")

    response = model.generate_content(
        content_parts,
        generation_config=genai.types.GenerationConfig(temperature=0.3),
    )

    formatted = {
        "model": model_name,
        "choices": [{"message": {"content": response.text}}]
    }
    return formatted, history


def _generate_openai(history, model_name, screenshot):
    """Generate using OpenAI-compatible API (OpenAI, Groq, Ollama, etc.)."""
    messages = list(history)

    # Add screenshot as base64 image if vision is supported
    if screenshot is not None and VISION_ENABLED:
        import base64
        from io import BytesIO
        buf = BytesIO()
        screenshot.save(buf, format='PNG')
        b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": "Here is the current annotated screenshot:"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
            ]
        })
        print("[UIAutomator Viewer] Annotated screenshot included in prompt")

    response = _client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.3,
    )

    formatted = {
        "model": response.model,
        "choices": [{"message": {"content": response.choices[0].message.content}}]
    }
    return formatted, history


def _generate_vertex(history, model_name, screenshot):
    """Generate using Vertex AI REST API — bills Google Cloud credits.
    Uses the same generateContent format as AI Studio but via aiplatform.googleapis.com.
    Supports the AQ.* API key format from Google Cloud Console.
    """
    import base64
    from io import BytesIO

    base_url = LLM.get('base_url', 'https://aiplatform.googleapis.com/v1/publishers/google/models')
    url = f"{base_url}/{model_name}:generateContent?key={LLM['api_key']}"

    # Build contents from history
    contents = []
    for msg in history:
        role = msg['role']
        content = msg['content']
        if role == 'system':
            # Vertex AI doesn't have system role — prepend as user turn
            contents.append({"role": "user", "parts": [{"text": f"[System]: {content}"}]})
            contents.append({"role": "model", "parts": [{"text": "Understood."}]})
        elif role == 'assistant':
            contents.append({"role": "model", "parts": [{"text": content}]})
        else:
            contents.append({"role": "user", "parts": [{"text": content}]})

    # Append screenshot to last user turn if available
    if screenshot is not None and VISION_ENABLED:
        buf = BytesIO()
        screenshot.save(buf, format='PNG')
        b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        if contents and contents[-1]['role'] == 'user':
            contents[-1]['parts'].append({
                "inline_data": {"mime_type": "image/png", "data": b64}
            })
        else:
            contents.append({"role": "user", "parts": [
                {"text": "Here is the current annotated screenshot:"},
                {"inline_data": {"mime_type": "image/png", "data": b64}},
            ]})
        print("[UIAutomator Viewer] Annotated screenshot included in prompt")

    payload = {
        "contents": contents,
        "generationConfig": {"temperature": 0.3},
    }

    response = _requests.post(url, json=payload, timeout=120)
    response.raise_for_status()
    data = response.json()

    text = data["candidates"][0]["content"]["parts"][0]["text"]
    formatted = {
        "model": model_name,
        "choices": [{"message": {"content": text}}]
    }
    return formatted, history


# ── Helpers ──────────────────────────────────────────────────────────────────

def save_chat_history(history, package_name):
    os.makedirs('./chat_history', exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    path = f"./chat_history/{package_name}_chat_{ts}.json"
    with open(path, 'w') as f:
        json.dump(history, f)

def get_model_name(response):
    return response["model"]

def get_message(response):
    return response["choices"][0]["message"]["content"]
