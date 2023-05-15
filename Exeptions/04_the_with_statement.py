try:
    with open("03_cleaning_up.py") as file:
        print("file opened.")
# its works with statement as a file name as file.

    age = int(input("Age: "))
    xfactor = 10/age


except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No execptions were thrown")
