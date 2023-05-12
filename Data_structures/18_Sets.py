numbers = [1, 1, 2, 2, 3, 4]
uniques = set(numbers)

second = {1, 4}
second.add(5)
# second.remove(5)
print(len(second))

print(uniques | second)
# using these code line we can get union of both sets

print(uniques & second)
# we can get both exist one

print(uniques - second)
# different between two sets

# we can't call index on sets becouse we use if statement
if 1 in uniques:
    print("yes")


print(uniques ^ second)
# not exists atleast one set

# print(uniques)
# set function is mostly use for filter the unique numbers
