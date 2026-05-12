# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return true if you're better, else false!
# Note:
# Your points are not included in the array of your class's points. Do not forget them when calculating the average score!
def better_than_average(class_points, your_points):
    return sum(class_points) / len(class_points) < your_points


if __name__ == "__main__":
    print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))  # True
    print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))  # True
    print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))  # False
