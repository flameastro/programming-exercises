# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.
# Solution 1
def correct(s):
    return s.replace("5", "S").replace("0", "O").replace("1", "I")


# Solution 2
def correct(s):
    cs = ""

    for l in s:
        if l == "5":
            cs += "S"
        elif l == "0":
            cs += "O"
        elif l == "1":
            cs += "I"
        else:
            cs += l

    return cs


if __name__ == "__main__":
    print(correct("L0ND0N"))  # LONDON
    print(correct("DUBL1N"))  # DUBLIN
    print(correct("51NGAP0RE"))  # SINGAPORE
