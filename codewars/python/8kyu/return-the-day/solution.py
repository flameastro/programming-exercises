# Complete the function which returns the weekday according to the input number:
# 1 returns "Sunday"
# 2 returns "Monday"
# 3 returns "Tuesday"
# 4 returns "Wednesday"
# 5 returns "Thursday"
# 6 returns "Friday"
# 7 returns "Saturday"
# Otherwise returns "Wrong, please enter a number between 1 and 7"

def whatday(num):
    return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][num-1] if num in range(1, 8) else "Wrong, please enter a number between 1 and 7"


if __name__ == '__main__':
    print(whatday(1))  # Sunday
    print(whatday(2))  # Monday
    print(whatday(3))  # Tuesday
