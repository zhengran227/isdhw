class Dimension:
    def_init_(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        pass
class Ellipse(Dimension):
    def_init_(self,m,n):
        Dimension._init_(self,m,n)
    def area(self):
        return 3.14*self.x*self.y
class Square(Dimension):
    def_init_(self,q):
        Dimension._init_(self,q,0)
    def area(self):
        return self.x*self.x

class Circle(Dimension):
    def_init_(self,r):
        Dimension._init_(self,r,0)
    def area(self):
        return 3.14*self.x*self.x

class Rectangle(Dimension):
    def_init_(self,w,h):
        Dimension._init_(self,w,h)
    def area(self):
        return self.x*self.y

shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]
total_area = compute_area(shapes)
    print(total_area)
