class Point:

    def __init__(self, x, y):
        # becouse we use init, it will run automatically
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    # if we use any magic method it will run smoothly

    # def draw(self):
    #     print(f"Point ({self.x},{self.y})")


point = Point(1, 2)
print(point)
