print(1)
#write a simple code so that i can genearte the uml diagram for it
#I am using pyreverse for this
from abc import ABC, abstractmethod
from typing import List
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width
    
    def perimeter(self) -> float:
        return 2 * (self.length + self.width)
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius
#now i can generate the uml diagram for this code
#pyreverse -o png -p my_shapes my_shapes.py
#this will generate the uml diagram for the code
#now i can use this uml diagram to understand the code
#and also to generate the code from the uml diagram
