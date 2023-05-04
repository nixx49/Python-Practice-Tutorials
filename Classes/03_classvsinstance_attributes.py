class Point:
    default_color = "red"
    # this is a class level attribue

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


Point.default_color = "yellow"
# if we use this default color is changed as yellow
# class level attributes are shared
# all instances of class

point = Point(1, 2)
print(Point.default_color)
print(Point.default_color)
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()
