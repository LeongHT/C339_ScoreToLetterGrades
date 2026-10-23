def score_to_letter_grade(score):
    if score >= 80:
        return "A"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "D+"
    elif score > 50:
        return "D"
    else:
        return "F"


def main():
    score = float(input("Enter the score: "))
    grade = score_to_letter_grade(score)
    print(f"Letter grade: {grade}")


if __name__ == "__main__":
    main()
