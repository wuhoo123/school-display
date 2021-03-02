# - the string "threefive", if x is a multiple of both 3 and 5.
# - the string "three", if x is a multiple of 3 and not 5.
# - the string "five", if x is a multiple of 5 and not 3.
# - the integer x, if x is not divisible by either 3 or 5.

def student_func(x):
    if x%15 == 0:
        return "threefive"
    elif x%3 == 0:
        return "three"
    elif x%5 == 0:
        return "five"
    else:
        return x




    pass

print(student_func(10))