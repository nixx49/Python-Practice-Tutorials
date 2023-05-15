from timeit import timeit
# using timeit function we can calculate execution time


code1 = """
def calculate(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
        # exeption raise on here
    return 10/age


# its handles on here
try:
    calculate(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate(age):
    if age <= 0:
        return None
        # exeption raise on here
    return 10/age


xfactor = calculate(-1)
if xfactor == None:
    pass

"""
print("frist code = ", timeit(code1, number=1000))
print("second code = ", timeit(code2, number=1000))

# code two has low executing time than frist code
