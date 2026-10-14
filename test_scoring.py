"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

import pytest

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


# TODO: add at least one more test, e.g. a boundary case for "Skip" (a score
# of 59) or the exact boundary for "Good" (a score of 80).
def test_session_rating_boundary_61_is_meh():
    assert session_rating(61) == "Meh"

# --- Part 3: breaker inputs -------------------------------------------------
# Decision for all four: FLAG OUT OF SCOPE, do not add validation.
# No caller can produce these -- apply_streak_bonus() caps at 100, and the
# slider/number_input bounds can't go negative or fractional. Guarding inside
# session_rating() would be dead code and would duplicate the 100-cap.
# These tests pin the current behavior so that if someone later removes that
# upstream guarantee, the assumption fails loudly instead of quietly.

def test_negative_score_falls_through_to_skip():
    """-50 -> "Skip": right answer, but by fall-through, not by a guard."""
    assert session_rating(-50) == "Skip"


def test_score_above_100_still_rates_great():
    """150 -> "Great": unreachable while apply_streak_bonus() caps at 100."""
    assert session_rating(150) == "Great"


def test_float_accepted_despite_int_type_hint():
    """87.5 -> "Good": the `int` hint is documentation, not a runtime check."""
    assert session_rating(87.5) == "Good"


def test_non_numeric_input_raises_type_error():
    """The only breaker that actually breaks -- and no caller can reach it."""
    with pytest.raises(TypeError):
        session_rating("90")
