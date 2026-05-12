# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"
def number_to_string(num):
    return str(num)

if __name__ == "__main__":
    print(number_to_string(1), type(number_to_string(1)))  # -1 <class 'str'>
    print(number_to_string(14), type(number_to_string(14)))  # -14 <class 'str'>
    print(number_to_string(-34), type(number_to_string(-34)))  # 34 <class 'str'>
