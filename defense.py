from target_bot import REFUSAL, output_filter
from judge import judge


def layered_filter(answer):
    # Layer 1: cheap text rules (secret code and confidential lines).
    filtered = output_filter(answer)
    if filtered != answer:
        return filtered
    # Layer 2: the LLM judge, which can also catch translated or reworded leaks.
    leaked, _ = judge(answer)
    if leaked:
        return REFUSAL
    return answer
