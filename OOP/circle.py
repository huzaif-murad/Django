class Circle:
    def __init__(self,r):
        self.r=r
    
    def area(self):
        circleArea=3.14*self.r*self.r
        return circleArea

    def perimeter(self):
        circlePerimeter=2*3.14*self.r
        return circlePerimeter

c=Circle(5)

print(c.area())
print(c.perimeter())