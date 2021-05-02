class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rect(self):
        return f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})'

a = Rectangle(5, 10, 50, 100)
print(a.get_rect())