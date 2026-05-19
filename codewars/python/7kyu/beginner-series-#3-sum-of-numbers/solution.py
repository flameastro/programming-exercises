# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.
# Note: a and b are not ordered!
# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
# Your function should only return a number, not the explanation about how you get that number.
def get_sum(a, b):
    return sum([x for x in range(a, b+1)]) if a < b else sum([x for x in range(b, a+1)]) 


if __name__ == "__main__":
    print(get_sum(0, 1))  # 1
    print(get_sum(2, 5))  # 14
    print(get_sum(2, -8))  # -33
