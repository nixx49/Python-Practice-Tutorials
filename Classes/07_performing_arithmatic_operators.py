class Add:
    def __init__(self, x, y):
        # since init function it is automatically run
        # it gets given x value and y value of frist object
        self.x = x
        self.y = y

    def __add__(self, other):
        # self.x gives frist object data
        # and other gives other object data
        return Add(self.x + other.x, self.y + other.y)


point = Add(10, 20)  # object one
other = Add(1, 2)  # object two
combined = point + other  # create new object as combined to add both x and y value

print(f"OUTPUT ({combined.x},{combined.y})")
# print(combined.y)
