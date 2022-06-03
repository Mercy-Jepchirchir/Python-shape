
# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr
class Circle:
    def __init__(self,radius):
        self.radius=radius
     
    def area_of_a_circle(self):
        area=3.142*self.radius**2
        return f"The area is {area}"
    def circumference (self):
        cir= (self.radius+self.radius)*3.142
        return f"The perimeter is {cir}"
    
#     Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a
    
    
class Square: 
    def __init__(self,side):
        self.side = side
        
    def area_of_square(self):
        A = self.side*self.side
        return f"the area of the square is: {A}"
    
    def perimeter (self):
        P = 4*self.side
        return f"the perimeter of the square {P}"
#Class Rectangle
#A Rectangle instance accepts two sides of a rectangle (w,l)
#It has method to calculate the area (A) of the rectangle using the formula A=wl
#It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)
    
class Rectangle:
    def __init__(self,l,w):
        self.w=w
        self.l=l
        
    def area_of_rectangle(self):
        Area = self.w*self.l
        return f"the area of rectangle is {Area}"
    
    def perimeter_of_rectangle(self):
        per = 2(self.l+self.w)
        return f"the perimeter of rectangle is {per}"
    
   # Class Sphere
#A Sphere Instance accepts the radius of the sphere (r)
#It has a method to calculate the surface area (A) using the formula A=4πr2
#It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)
    
class Sphere:
    def __init__(self,r_sphere):
        self.r_sphere = r_sphere
        
    def surface_area(self):
        S_A = 4*self.r_sphere**2*3.142
        return  f"the surface area of sphere is {S_A}"
    
    def volume(self):
        V= 1.333*3.142*self.r_sphere**3
        return f"the volume of the sphere is {V}"
        
        
    
    