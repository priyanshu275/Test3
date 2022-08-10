from abc import ABC, abstractmethod
import math
class Epolygon(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class ERectangle(Epolygon):
    def __init__(self):
        side = int(input("plz provide value of side of rectangle"))
        self.side = side
    def area(self):
       print(pow(self.side,2))
    def perimeter(self):
        print(4*self.side)

class ESquare(Epolygon):
    def __init__(self):
        side = int(input("plz provide value of side of square"))
        self.side = side
    def area(self):
       print(pow(self.side,2))
    def perimeter(self):
        print(4*self.side)

class Epentagon(Epolygon):
    def __init__(self):
        side=int(input("plz provide value of side of regular pentagon"))
        self.side=side
    def area(self):
        b=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(self.side, 2))/4
        print(b)
    def perimeter(self):
        print(5*self.side)
p=Epentagon()
p.area()










