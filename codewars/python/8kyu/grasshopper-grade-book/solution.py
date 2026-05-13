# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
def get_grade(s1, s2, s3):
    score = sum([s1, s2, s3]) / 3
    return "A" if score <= 100 and score >= 90 else "B" if score < 90 and score >= 80 else "C" if score < 80 and score >= 70 else "D" if score < 70 and score >= 60 else "F"


if __name__ == "__main__":
    print(get_grade(15, 65, 54))  # F
    print(get_grade(96, 98, 97))  # A
    print(get_grade(89, 77, 89))  # B
