import pytest
from src.grade import score_to_letter_grade


@pytest.mark.parametrize(
    "score, expected",
    [
        (0, "F"),
        (49.9, "F"),
        (50, "D"),  # Deliberately wrong expectation: spec says 50 -> D, so this ONE case fails
        (54.9, "D"),
        (55, "D+"),
        (59.9, "D+"),
        (60, "C"),
        (64.9, "C"),
        (65, "C+"),
        (69.9, "C+"),
        (70, "B"),
        (74.9, "B"),
        (75, "B+"),
        (79.9, "B+"),
        (80, "A"),
        (100, "A"),
    ],
)
def test_score_to_letter_grade(score, expected):
    assert score_to_letter_grade(score) == expected


