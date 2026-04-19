# Solution 1
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s


# Solution 2
def disemvowel(string):
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    answer = ""
    for letter in string:
        if not letter in vowels:
            answer += letter
    return answer
