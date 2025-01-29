#create class
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    def area(self):
        return print("Area of the rectangle: " + str(self.length * self.width))
        
#create object and call functions
rect = Rectangle(5, 3)
rect.area()



    