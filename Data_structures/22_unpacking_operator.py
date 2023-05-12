# print individual numbers in list
numbers = [1, 2, 3]
print(*numbers)

values = list(range(5))
values = [*range(5), *"hello"]
print(*values)

first = [1, 2]
second = [3]

new = [*first, "a", *second, "b"]
print(*new)

one = {"x": 1}
two = {"x": 10, "y": 2}
combined = {**one, **two, "z": 1}
print(combined)
