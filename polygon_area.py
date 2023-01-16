class Rectangle:

    def __init__ (self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
    
    def __repr__(self):
        name = "Rectangle(width=" + str(self.ancho) + ", height=" + str(self.largo) + ")"
        return(name)
    
    def set_width(self, ancho_2):
        self.ancho = ancho_2
        return(self.ancho)

    def set_height(self, largo_2):
        self.largo = largo_2
        return(self.largo)
    
    def get_area (self):
        self.area = self.ancho * self.largo
        return(self.area)
    
    def get_perimeter(self):
        perimetro = 2 * self.ancho + 2 * self.largo
        return(perimetro)

    def get_diagonal(self):
        diagonal = (self.ancho ** 2 + self.largo ** 2) ** 0.5
        return(diagonal)
    
    def get_picture(self):
      
        if self.ancho <= 50 and self.largo <= 50:
            picture = (('*' * self.ancho) + '\n') * self.largo
            return(picture)
        else:
            return('Too big for picture.')

    def get_amount_inside(self, shape):
        amount_inside = int(self.get_area() / shape.get_area())
        return(amount_inside)



class Square(Rectangle):

    def __init__ (self, side):
       self.ancho = side
       self.largo = side

    def __repr__(self):
        name = "Square(side=" + str(self.ancho) + ")"
        return(name)

    def set_side(self, side_2):
        self.ancho = side_2
        self.largo = side_2
        return(self.ancho)
    


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(51)
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

rect.set_width(51)
rect.set_height(3)
print(rect.get_picture())
        
#https://replit.com/@EyckVanJan/polygon-area-calculator?v=1