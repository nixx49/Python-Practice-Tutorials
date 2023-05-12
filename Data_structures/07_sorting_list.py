numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
# it can sort given list in reverse order

# we can remove reverse=true then sorted as small to big one
print(sorted(numbers, reverse=True))
# it can make new sorted list using "sorted" function
print(numbers)

items = [  # this type of lists, python can't access directly
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 11),
    ("Product1", 12),
]


def sort_item(item):  # initialize argument as "item"
    return item[1]  # get the second index as a key


items.sort(key=sort_item, reverse=True)
# apply item[1] index to items list as a key
# sort it in asending order
print(items)  # print the item list
