# Write a function that always returns 5
# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/
# Good luck :)
def unusual_five():
    return sum([x for x in [True, True, True, True, True]])



if __name__ == "__main__":
    print(unusual_five())  # 5
