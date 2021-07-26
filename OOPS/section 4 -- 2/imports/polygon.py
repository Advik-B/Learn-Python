class Polygon:
    __width = None
    __height = None
    
    def set_value(self,height,width):
        self.__width = width
        self.__height = height
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height

class Square(Polygon):
    def area(self):
        return self.get_width() * self.get_height()





class Triangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height() * 1/2

sq = Square()

# sq.set_value(8,16)

# print (sq.area())

t = Triangle()