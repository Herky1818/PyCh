class Rectangle:
    def __init__(self,length,breadth,Cost=0):
        self.length=length
        self.breadth=breadth
        self.Cost=Cost
    def get_area(self):
        return self.length*self.breadth
    def get_Cost(self):
        area=self.get_area()
        return area*self.Cost
    def get_perimeter(self):
        return 2*(self.length+self.breadth)
r=Rectangle(12,34,500)
print("Area of Rectangle: ", (r.get_area()))
print("Cost of Area: ", (r.get_Cost()))
print("Perimeter of Rect: ", (r.get_perimeter()))