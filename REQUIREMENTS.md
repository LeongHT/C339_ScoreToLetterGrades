# Requirements: Score to Letter Grade

## Functional
| ID | Requirement |
|----|-------------|
| R1 | `score_to_letter_grade(score)` converts a Module Grade raw score (%) to a letter grade. |
| R2 | Mapping (lower bound inclusive, upper bound exclusive): |

| Raw score | Letter grade |
|-----------|--------------|
| < 50      | F  |
| 50 to < 55 | D  |
| 55 to < 60 | D+ |
| 60 to < 65 | C  |
| 65 to < 70 | C+ |
| 70 to < 75 | B  |
| 75 to < 80 | B+ |
| 80 and above | A |

| ID | Requirement |
|----|-------------|
| R3 | Decimal scores are supported (e.g. 54.9 -> D, 55.0 -> D+). |

## Non-functional
- Python 3.8+, no third-party dependencies (tests use `pytest`).
