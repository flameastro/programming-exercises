# Solution 1
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)


# Solution 2
def is_triangle(a, b, c):
    if(a <= 0 | b <= 0 | c <= 0):
        return False
    elif( a + b <= c or a + c <= b or b + c <= a): 
        return False
    else:
        return True


# Solution 3
def is_triangle(a, b, c):
    return 2 * max(a, b, c) < a + b + c
