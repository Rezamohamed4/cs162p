class Point:
    def __init__(self, symbol):
        self.symbol = symbol

    def setSymbol(self, symbol):
        self.symbol = symbol

    def draw(self):
        print(self.symbol)

class Triangle(Point):
    def __init__(self, symbol, size):
        super().__init__(symbol)
        self.size = size

    def draw(self):
        # Implementation for drawing a triangle

class Diamond(Point):
    def __init__(self, symbol, width, height):
        super().__init__(symbol)
        self.width = width
        self.height = height

    def draw(self):
        # Implementation for drawing a diamond

class Rectangle(Point):
    def __init__(self, symbol, width, height):
        super().__init__(symbol)
        self.width = width
        self.height = height

    def draw(self):
        # Implementation for drawing a rectangle

class Square(Rectangle):
    def __init__(self, symbol, size):
        super().__init__(symbol, size, size)

    def draw(self):
        # Implementation for drawing a square
