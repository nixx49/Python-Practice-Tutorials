from sys import getsizeof

values = (x * 2 for x in range(10000))
print("gen", getsizeof(values))

values = [x * 2 for x in range(10000)]
print("list", getsizeof(values))
# gen function in list
# we cant gen length of this
# only can access values
