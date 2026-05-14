# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.
# For example, a tower with 3 floors looks like this:
# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:
# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]
# Go challenge Build Tower Advanced once you have finished this :)
def tower_builder(n_floors):
    l = []
    n = 1
    for x in range(n_floors-1, -1, -1):
        l.append(f"{' ' * x}{'*' * n}{' ' * x}")
        n += 2

    return l


if __name__ == "__main__":
    print(tower_builder(1))  # ['*']
    print(tower_builder(3))  # ['  *  ',
    # ' *** ',
    # '*****'
    # ]
    print(tower_builder(6))  # ['     *     ',
    # '    ***    ',
    # '   *****   ',
    # '  *******  ',
    # ' ********* ',
    # '***********'
    # ]

