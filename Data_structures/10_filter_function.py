items = [
    ("product", 10),
    ("product1", 9),
    ("product", 12),
    ("product", 11)
]

# it can filter price >= 10 lists
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
