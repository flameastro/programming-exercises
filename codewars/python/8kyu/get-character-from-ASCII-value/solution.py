# Write a function which takes a number and returns the corresponding ASCII char for that value.
# Example:
# 65 --> 'A'
# 97 --> 'a'
# 48 --> '0
# For ASCII table, you can refer to http://www.asciitable.com/

def get_char(c):
    return chr(c)


if __name__ == "__main__":
    print(get_char(65))  # A
    print(get_char(97))  # a
    print(get_char(48))  # 0
