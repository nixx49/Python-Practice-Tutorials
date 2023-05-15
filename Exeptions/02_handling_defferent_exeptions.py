try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("you didn't enter valid age")
# except ZeroDivisionError:
#     print("zero is not valid")
else:
    print("no exeptions were thrown")
