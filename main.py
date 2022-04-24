class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        full_picture = ''
        for vertical in range(self.width):
            full_picture += "*" * self.height
            full_picture += "\n"
        
        return full_picture
    
    def get_amount_inside(self, object):
        area = self.get_area()
        object_area = object.get_area()

        num_of_input = area // object_area
        return num_of_input
    
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length

    def _side_changes(self, length):
        self.width = length
        self.height = length

    def set_side(self, length):
        self._side_changes(length)
    
    def set_width(self, length):
        self._side_changes(length)
    
    def set_height(self, height):
        self._side_changes(length)

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"


rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))