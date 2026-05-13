# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

# Constraint:

# 1 <= month <= 12
def quarter_of(month):
    return 1 if month in range(1, 4) else 2 if month in range(4, 7) else 3 if month in range(7, 10) else 4


if __name__ == "__main__":
    print(quarter_of(3))  # 1
    print(quarter_of(8))  # 3
    print(quarter_of(11))  # 4
