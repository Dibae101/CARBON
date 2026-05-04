"""
LLM Provider Configuration — Switch between Gemini, OpenAI, Groq, etc.

Usage in .env:
    LLM_PROVIDER=gemini          # or openai, groq
    LLM_API_KEY=your_key_here
    LLM_MODEL=gemini-2.5-pro     # optional, uses default if not set
"""

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# ── Read from .env ───────────────────────────────────────────────────────────

PROVIDER = os.getenv('LLM_PROVIDER', 'gemini').lower()
API_KEY = os.getenv('LLM_API_KEY', os.getenv('GEMINI_API_KEY', ''))
MODEL = os.getenv('LLM_MODEL', '')

# ── API Key Rotation ────────────────────────────────────────────────────────
# Load all available API keys for automatic rotation on quota exhaustion.
# Keys are read from LLM_API_KEY, LLM_API_KEY2, LLM_API_KEY3, etc.

API_KEYS = []
if API_KEY:
    API_KEYS.append(API_KEY)
for i in range(2, 20):
    k = os.getenv(f'LLM_API_KEY{i}', '')
    if k:
        API_KEYS.append(k)

_current_key_index = 0

# ── Provider configs ─────────────────────────────────────────────────────────

PROVIDERS = {
    'gemini': {
        'type': 'gemini',           # uses google-generativeai library
        'default_model': 'gemini-2.5-pro',
        'max_tokens': 128000,
        'supports_vision': True,
    },
    'openai': {
        'type': 'openai',           # uses openai library
        'base_url': 'https://api.openai.com/v1',
        'default_model': 'gpt-4o',
        'max_tokens': 128000,
        'supports_vision': True,
    },
    'groq': {
        'type': 'openai',           # groq uses openai-compatible API
        'base_url': 'https://api.groq.com/openai/v1',
        'default_model': 'llama-3.3-70b-versatile',
        'max_tokens': 32768,
        'supports_vision': False,
    },
    'gemini-openai': {
        'type': 'openai',           # gemini via openai-compatible endpoint
        'base_url': 'https://generativelanguage.googleapis.com/v1beta/openai/',
        'default_model': 'gemini-2.5-pro',
        'max_tokens': 128000,
        'supports_vision': True,
    },
    'vertex': {
        'type': 'vertex',           # Vertex AI REST API — bills Google Cloud credits
        'base_url': 'https://aiplatform.googleapis.com/v1/publishers/google/models',
        'default_model': 'gemini-2.5-pro',
        'max_tokens': 128000,
        'supports_vision': True,
    },
    'ollama': {
        'type': 'openai',           # ollama uses openai-compatible API
        'base_url': 'http://localhost:11434/v1',
        'default_model': 'llama3',
        'max_tokens': 8192,
        'supports_vision': False,
    },
}

# ── Resolve config ───────────────────────────────────────────────────────────

def get_config():
    """Get the active LLM configuration."""
    if PROVIDER not in PROVIDERS:
        raise ValueError(f"Unknown LLM_PROVIDER: {PROVIDER}. Options: {list(PROVIDERS.keys())}")

    config = dict(PROVIDERS[PROVIDER])
    config['api_key'] = API_KEYS[_current_key_index] if API_KEYS else API_KEY
    config['model'] = MODEL or config['default_model']
    config['provider'] = PROVIDER

    if not config['api_key']:
        raise ValueError(f"LLM_API_KEY not set in .env for provider '{PROVIDER}'")

    return config


def rotate_key():
    """Rotate to the next API key. Returns True if rotated, False if no more keys."""
    global _current_key_index
    if len(API_KEYS) <= 1:
        return False
    old_idx = _current_key_index
    _current_key_index = (_current_key_index + 1) % len(API_KEYS)
    old_key = API_KEYS[old_idx][:12]
    new_key = API_KEYS[_current_key_index][:12]
    print(f"[Key Rotation] Switching from key {old_idx+1} ({old_key}...) "
          f"to key {_current_key_index+1} ({new_key}...) "
          f"[{_current_key_index+1}/{len(API_KEYS)}]")
    return True


def get_current_key_info():
    """Return info about current key for logging."""
    return f"key {_current_key_index+1}/{len(API_KEYS)} ({API_KEYS[_current_key_index][:12]}...)"


# Print config when imported (for debugging)
if __name__ == '__main__':
    c = get_config()
    print(f"Provider:  {c['provider']}")
    print(f"Type:      {c['type']}")
    print(f"Model:     {c['model']}")
    print(f"Vision:    {c['supports_vision']}")
    print(f"Key:       {c['api_key'][:12]}...")
    print(f"Total keys: {len(API_KEYS)}")
    for i, k in enumerate(API_KEYS):
        marker = " (active)" if i == _current_key_index else ""
        print(f"  Key {i+1}: {k[:12]}...{marker}")
