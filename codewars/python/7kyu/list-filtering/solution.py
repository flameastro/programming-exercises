# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
# Solution 1
def filter_list(l):
    return [e for e in l if type(e).__name__ == "int"]

# Solution 2:
def filter_list(l):
    return [e for e in l if e != str(e)]


if __name__ == "__main__":
    print(filter_list([1,2,'a','b']))  # [1, 2]
    print(filter_list([1,'a','b',0,15]))  # [1, 0, 15]
    print(filter_list([1,2,'aasf','1','123',123]))  # [1, 2, 123]
