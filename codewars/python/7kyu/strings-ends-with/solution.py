# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples:
# Inputs: "abc", "bc"
# Output: true
# Inputs: "abc", "d"
# Output: false
def solution(text, ending):
    return text.endswith(ending)


if __name__ == "__main__":
    print(solution("Hello", "World"))  # False
    print(solution("abcdef", "def"))  # True
    print(solution("123456", "654321"))  # False
