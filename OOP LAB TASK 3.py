class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: {self.width} x {self.height}"
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
rect1 = Rectangle(10.0, 20.0)
print(rect1)  
print(f"Area: {rect1.area()}")  
print(f"Perimeter: {rect1.perimeter()}")
