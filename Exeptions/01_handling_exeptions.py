try:
    age = int(input("Age: "))
except ValueError as ex:  # as x optional
    print("You didn't enter a valid age")
    print(ex)  # print the error
    print(type(ex))  # print the error type
else:
    print("No exeptions")
print("Execution continues")
