# example_dict = {"key1":"value1", "key2":"value2", "key3":"value3"}
# print("key4" in example_dict)
# print("value1" in example_dict)
# print("key1" in example_dict)
# print(("key2", "value2") in example_dict)




def student_func(x):
    y = x.lower()
    y = y.replace(" ", "")
    z = y[::-1]
    if z == y:
        return True
    return False
    # `x` is a string
    # this function should return either `True` or `False`

    # write your code here
    # be sure to include a `return` statement so that
    # your function returns the appropriate object.
    pass


print(student_func("dejcne"))