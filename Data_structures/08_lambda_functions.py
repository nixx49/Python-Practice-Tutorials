items = [  # this type of lists, python can't access directly
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 11),
    ("Product4", 12),
]

# lambda function can carry any number of arguments
# its a anonymous function

items.sort(key=lambda item: item[1])
# but one only have one expression
# "parameters:expression"

print(items)
