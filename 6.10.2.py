class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_rect_area(self):
        return self.width * self.height

    def get_rect_perim(self):
        return self.width * 2 + self.height * 2

rectangle = Rectangle(80, 60)
print(rectangle.get_rect_area())
print(rectangle.get_rect_perim())
