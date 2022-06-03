


class circle:
    PI = 3.142 
    
    def __init__(self,radius):
        self.radius = radius
        
    def area (self):
        return (circle.PI * self.radius * self.radius)#nr2
    
    def circumference (self):
        return (2 * circle.PI *self.radius)#2nR  

c1=float(input("Enter the radius of a circle: "))
objcircle=circle(c1)
print ("Area of c1 circle is: ", objcircle.area())
print ("circumference of c1 circle is: ",objcircle.circumference())


class quare:
    
    def __init__(self, a):
        self.a = a
        
    def s_area (self): #a^2
        return (self.a * self.a)
    
    def __init__(self, a):
        self.a = a
        
    def s_area (self): #a^2
        return (self.a * self.a)
    
    def perimeter (self):
        return (self.a * 4)
    def perimeter (self):
        return (self.a * 4)
     
s=float(input("Enter the length of the Side : "))
s_area=s*s
perimeter=4*s
print("Area of square is: ",s_area)
print("Perimeter of square is : ",perimeter)


class rectangle:
    def __init__(self,length,widtth):
        self.length = length
        self.widtth = widtth
        
    def calc_area(self):
        return (self.length*self.widtth)
        
    def calculate_perimeter(self):
        return (2*(self.widtth +self.length))

l = float(input("Enter length of the rectangle: "))
w = float(input("Enter width of the rectangle: "))
calc_area= l*w
total=l+w
calculate_perimeter=2*total
print(f"Area of the rectangle is:{calc_area} ")
print(f"perimeter of the rectangle is: {calculate_perimeter}")
    

        
    