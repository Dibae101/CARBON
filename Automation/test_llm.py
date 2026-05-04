#!/usr/bin/env python3
"""Quick test to verify LLM connection based on .env settings."""

import sys, time
from llm_config import get_config

config = get_config()
print(f"Provider:  {config['provider']}")
print(f"Model:     {config['model']}")
print(f"Type:      {config['type']}")
print(f"Vision:    {config['supports_vision']}")
print(f"Key:       {config['api_key'][:12]}...")
print()

try:
    start = time.time()

    if config['type'] == 'gemini':
        import google.generativeai as genai
        genai.configure(api_key=config['api_key'])
        model = genai.GenerativeModel(f"models/{config['model']}")
        response = model.generate_content("Say hello in one sentence.")
        reply = response.text

    elif config['type'] == 'openai':
        from openai import OpenAI
        client = OpenAI(api_key=config['api_key'], base_url=config.get('base_url'))
        response = client.chat.completions.create(
            model=config['model'],
            messages=[{"role": "user", "content": "Say hello in one sentence."}],
            temperature=0.3,
        )
        reply = response.choices[0].message.content

    elapsed = time.time() - start
    print(f"✅ Connected! ({elapsed:.1f}s)")
    print(f"Response: {reply.strip()}")

except Exception as e:
    print(f"❌ Failed: {e}")
    sys.exit(1)
