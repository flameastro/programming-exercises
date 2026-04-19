# Solution 1
import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


# Solution 2
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())
