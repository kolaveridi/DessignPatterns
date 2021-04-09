import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass
    
    @abc.abstractmethod
    def calculate_perimeter(self):
        pass
    
    
    
class Rectangle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width
    
    def calculate_area(self):
        return self.height*self.width
    
    def calculate_perimeter(self):
        return 2*(self.height+self.width)
    
    
    
    
        
class Square(Shape):
    def __init__(self,side):
        self.side =side
        
    def calculate_area(self):
        return self.side*self.side
    
    def calculate_perimeter(self):
        return 4*self.side
    
    
class ShapeFactory:
    def create_shape(self,shape):
        if shape == 'rectangle':
            height= input("Enter height of rectnagle")
            width =input("Enter width of rectnagle")
            return Rectangle(int(height),int(width))
        elif shape == 'square':
            side =input("Enter side of square")
            return Square(int(side))
    
               
               
def shapes_client():
    shapeObj =ShapeFactory()
    shape_type =input("Enter shape type")
    shape =shapeObj.create_shape(shape_type)
    print("Perimeter is ",shape.calculate_perimeter())
    print("Area is ",shape.calculate_area())
     
     
     
if __name__=="__main__":
    shapes_client()                  