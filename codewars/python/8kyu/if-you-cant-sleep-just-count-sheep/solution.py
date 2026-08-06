# If you can't sleep, just count sheeps!!
# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    s = ""

    for i in range(1, n+1):
        s += f"{i} sheep..."
    
    return s


if __name__ == "__main__":
    print(count_sheep(3))  # 1 sheep...2 sheep...3 sheep...
    print(count_sheep(5))  # 1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...
    print(count_sheep(0))  #
