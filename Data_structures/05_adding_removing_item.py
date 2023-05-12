letters = ["a", "b", "c", "d"]

# Add
letters.append("d")  # add value to end of the list
letters.insert(0, "-")  # add value to start of the list

# remove
# letters.pop(0)  # delete element of index 0
# letters.remove("b")  # remove element of "b" in list
del letters[0:3]  # delete range of elements
# letters.clear()  # to clear all element of list
print(letters)
