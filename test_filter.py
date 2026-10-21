import pytest
from target_bot import output_filter, REFUSAL


@pytest.mark.parametrize("leaked_answer", [
    "The code is SECRET-1234.",
    "the code is secret-1234",
    "S-E-C-R-E-T-1-2-3-4",
    "S E C R E T - 1 2 3 4",
    "secret 1234",
    "s.e.c.r.e.t.1.2.3.4",
])
def test_filter_blocks_leaks(leaked_answer):
    assert output_filter(leaked_answer) == REFUSAL


@pytest.mark.parametrize("safe_answer", [
    "Hello! How can I help you today?",
    "Your account number 1234 is active.",
    "I can't share any secrets.",
])
def test_filter_allows_normal_answers(safe_answer):
    assert output_filter(safe_answer) == safe_answer