class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        # using this statement we can compare both


point = Point(1, 2)
other = Point(1, 2)

print(point == other)
# if we use only this method, we cant get actual output
