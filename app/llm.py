# mocked LLM call – replace with provider SDK
import time
from random import random
from .metrics import TOKENS

def generate(prompt: str) -> str:
    # pretend token usage
    prompt_tokens = max(1, int(len(prompt) / 4))
    completion_tokens = 50
    TOKENS.labels("prompt").inc(prompt_tokens)
    TOKENS.labels("completion").inc(completion_tokens)

    # add random latency 0.2–1.8s
    time.sleep(0.2 + 1.6 * random())
    return f"Answer based on: {prompt[:80]}..."
