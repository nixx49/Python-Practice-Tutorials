# values = []
# for x in range(5):
#     values.append(x * 2)

# these both code sets are equal

values = {x: x * 2 for x in range(5)}
print(values)

# we can use dictionary compharison to list, sets, dictionaries
# cant use tuple
