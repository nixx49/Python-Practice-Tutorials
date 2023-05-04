high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Not eligible")
else:
    print("eligible")


# python logocal statements are short circuit.
# if its works untill one argument is falls.
# in given case high income is false. be/se it not work.
