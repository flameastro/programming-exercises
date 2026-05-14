# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# Input = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]
# Input = ["Peter", "Stephen", "Joe"]
# Output = []
def friend(x):
    return [name for name in x if len(name) == 4]


if __name__ == "__main__":
    print(friend(["Ryan", "Kieran", "Mark",]))  # ['Ryan', 'Mark']
    print(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]))  # ['Ryan']
    print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))  # ['Jimm', 'Cari', 'aret']
