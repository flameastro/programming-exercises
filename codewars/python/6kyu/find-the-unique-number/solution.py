# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.
# Slowed
# def find_uniq(arr):
#     return [n for n in arr if arr.count(n) == 1][0]

def find_uniq(arr):
    arr.sort()
    return arr[0] if arr[0] != arr[1] else arr[-1]


if __name__ == "__main__":
    print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))  # 2
    print(find_uniq([ 0, 0, 0.55, 0, 0 ]))  # 0.55
    print(find_uniq([ 3, 10, 3, 3, 3 ]))  # 10
