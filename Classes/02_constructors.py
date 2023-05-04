class Point:
    def __init__(self, x, y):
        # init is a constructor and it can
        # run automatically
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
