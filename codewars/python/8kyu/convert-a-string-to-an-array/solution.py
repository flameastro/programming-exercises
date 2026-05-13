# Write a function to split a string and convert it into an array of words.
# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
def string_to_array(s):
    return s.split()


if __name__ == "__main__":
    print(string_to_array("Robin Singh"))  # ['Robin', 'Singh']
    print(string_to_array("I love arrays they are my favorite"))  # ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
    print(string_to_array("1 2 3"))  # ['1', '2', '3']



