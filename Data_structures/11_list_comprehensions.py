items = [
    ("product", 10),
    ("product1", 9),
    ("product", 12),
    ("product", 11)
]


# prices = list(map(lambda item: item[1], items))
# print(sorted(prices))

prices = [item[1] for item in items]
# map a list to different kind of list
print(prices)

# it can filter price >= 10 lists
# filtered = list(filter(lambda item: item[1] >= 10, items))

# expression for item in items
filtered = [item for item in items if item[1] >= 10]
print(filtered)
