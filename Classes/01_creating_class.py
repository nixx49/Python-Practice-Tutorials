# class: blueprint for creating new object
# object: instance of a class

# class: Human
# Objects: John, Mary, Jack

# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))
# print(isinstance(point, Point))


class Phone:
    def say(self, name):
        self.x = name
        print("hello"+name)


phone1 = Phone()
phone1.say(" nokia")
print(phone1.x)

phone1.x = "apple"
print(phone1.x)

phone2 = Phone()
phone2.say(" samsung")
