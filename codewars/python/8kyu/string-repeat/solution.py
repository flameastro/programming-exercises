# Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.
# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"
def repeat_str(repeat, string):
    return string * repeat


if __name__ == "__main__":
    print(repeat_str(6, "I"))  # IIIIII
    print(repeat_str(5, "Hello"))  # HelloHelloHelloHelloHello
    print(repeat_str(12, "HA"))  # HAHAHAHAHAHAHAHAHAHAHAHA
