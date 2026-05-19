# Write a function that returns a string in which firstname is swapped with last name.
# Example(Input --> Output)
# "john McClane" --> "McClane john"
def name_shuffler(s):
    return " ".join(list(reversed(s.split())))


if __name__ == "__main__":
    print(name_shuffler("john McClane"))  # McClane john
    print(name_shuffler("Mary jeggins"))  # jeggins Mary
    print(name_shuffler("tom jerry"))  # jerry tom
