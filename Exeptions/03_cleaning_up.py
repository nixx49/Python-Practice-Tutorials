try:
    file = open("03_cleaning_up.py")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No execptions were thrown")
    # file.close()
finally:
    file.close()
# file is closed in end
# we not close in many time
