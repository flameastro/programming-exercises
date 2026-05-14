# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"



if __name__ == "__main__":
    print(even_or_odd(5))  # Odd
    print(even_or_odd(-3))  # Odd
    print(even_or_odd(0))  # Even
