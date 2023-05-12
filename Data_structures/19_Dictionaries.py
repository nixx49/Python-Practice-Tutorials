point = {"x": 1, "y": 2}
point["x"] = 10
point["z"] = 20

if "a" in point:
    print(point["a"])

# its return zero by default
print(point.get("a", 0))

# delete key_value from dictionary
del point["x"]
print(point)

# for loop in dictionary
# it will get result as a tuple
for x in point.items():
    print(x)

# we can unpacked tuple
# it returns value without tuple
for key, value in point.items():
    print(key, value)


# all()	    Return True if all keys of the dictionary are True (or if the dictionary is empty).
# any()	    Return True if any key of the dictionary is true. If the dictionary is empty, return False.
# len()	    Return the length (the number of items) in the dictionary.
# sorted()	Return a new sorted list of keys in the dictionary.
# clear()	Removes all items from the dictionary.
# keys()	Returns a new object of the dictionary's keys.
# values()	Returns a new object of the dictionary's values
