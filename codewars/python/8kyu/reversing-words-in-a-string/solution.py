# You need to write a function that reverses the words in a given string. Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
# Example (Input --> Output)
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
# Happy coding!

def reverse(st):
    return " ".join([x for x in st.split()][::-1])


if __name__ == "__main__":
    print(reverse("Hello World"))  # World Hello
    print(reverse("Hi There."))  # There. Hi
    print(reverse("Hi"))  # Hi
