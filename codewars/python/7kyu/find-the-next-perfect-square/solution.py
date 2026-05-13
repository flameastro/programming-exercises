# You might know some pretty large perfect squares. But what about the NEXT one?
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.
# Examples ( Input --> Output )
# 121 --> 144
# 625 --> 676
# 114 --> -1  #  because 114 is not a perfect square

# Solution 1
from math import sqrt
def find_next_square(sq):
    nsq = sqrt(sq)

    if nsq.is_integer():
        return int((nsq+1) ** 2)

    return -1


# Solution 2
from math import sqrt
def find_next_square(sq):
    return int((sqrt(sq)+1) ** 2 if sqrt(sq).is_integer() else -1)



if __name__ == "__main__":
    print(find_next_square(121))  # 144
    print(find_next_square(625))  # 676
    print(find_next_square(3232))  # -1
