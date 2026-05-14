# Messi goals function
# Messi is a soccer player with goals in three leagues:
# LaLiga
# Copa del Rey
# Champions
# Complete the function to return his total number of goals in all three leagues.
# Note: the input will always be valid.
# For example:
# 5, 10, 2  -->  17
# Solution 1
def goals(laLiga, copaDelRey, championsLeague):
    return sum([laLiga, copaDelRey, championsLeague])


# Solution 2
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague



if __name__ == "__main__":
    print(goals(2, 6, 5))  # 13
    print(goals(12, 21, 43))  # 76
    print(goals(15, 6, 12))  # 33

