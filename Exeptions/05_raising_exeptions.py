def calculate(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
        # exeption raise on here
    return 10/age


# its handles on here
try:
    calculate(-1)
except ValueError as error:
    print(error)
