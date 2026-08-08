# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
def solution(s):
    lt = [l for l in s]

    for i, x in enumerate(s):
        if x.isupper():
            lt.insert(i + len(lt)-len(s), " ")

    return "".join(lt)


if __name__ == "__main__":
    print(solution("camelCasing"))  # "camel Casing"
    print(solution("identifier"))  # "identifier"
    print(solution(""))  # ""
