
import math



class Figura :
    def area (self):
        pass
    def perimetre (self):
        pass

class Círculo(Figura) :
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        return math.pi *self.radio*self.radio

    def perimetre(self):
        return 2*math.pi *self.radio

class Triángulo(Figura)   :
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return (self.base*self.altura)/2
        
    def perimetre(self,a,b,c):
        return a+b+c

class Rectángulo(Figura)   :
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return self.base*self.altura
        
    def perimetre(self):
        return (self.base*2)+(self.altura*2)

class Cuadrado(Figura) :
    def __init__(self,costat ):
        self.costat =costat 
    
    def area(self):
        return self.costat *self.costat 
        
    def perimetre(self):
        return self.costat*4



cerc=Círculo(2)
trian=Triángulo (10,4)
rect=Rectángulo (8,9)
cuad=Cuadrado (5)

print("-----------------")
print("Area del Circulo :",cerc.area())
print("perimetre del Circulo :",cerc.perimetre())
print("-----------------")
print("Area del Triángulo  :",trian.area())
print("perimetre del Triángulo  :",trian.perimetre(2,5,7))
print("-----------------")
print("Area del Rectángulo  :",rect.area())
print("perimetre del Rectángulo  :",rect.perimetre())
print("-----------------")
print("Area del Cuadrado  :",cuad.area())
print("perimetre del Cuadrado  :",cuad.perimetre())