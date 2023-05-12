items = [
    ("product", 10),
    ("product1", 9),
    ("product", 12),
    ("product", 11)
]

# prices = []
# for item in items:  # for loop for use item in items
#     prices.append(item[1])  # a pre-defined method used to add a single item
#     # to certain collection types

# print(sorted(prices))
# print(prices)

prices = list(map(lambda item: item[1], items))
print(sorted(prices))
