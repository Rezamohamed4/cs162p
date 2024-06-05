from abc import ABC, abstractmethod

class Point(ABC):
    @abstractmethod
    def draw(self):
        pass

class Triangle(Point):
    def draw(self):
        # Implementation for drawing a triangle

class Diamond(Point):
    def draw(self):
        # Implementation for drawing a diamond

class Rectangle(Point):
    def draw(self):
        # Implementation for drawing a rectangle

class Square(Rectangle):
    def draw(self):
        # Implementation for drawing a square
