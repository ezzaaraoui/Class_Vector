import math
class Vecteur2D:
    _nbre = 0
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Vecteur2D._nbre += 1

    
    def getX(self):
        return self.__x       

    def setX(self ,x ):
        self.__x = x                              

    def getY(self):
        return self.__y
    
    def setY(self ,y ):
        self.__y = y    

    def getNbre(self):
        return self._nbre

    def ToString(self):
        return f"abscisse : {self.__x} \nordonne : {self.__y}"

    def Equals(self, vec):
        if self.__x == vec.getX() and  self.__y == vec.getY():
            return True
        else :
            return False

    def Norme(self):
        return math.sqrt(self.__x**2 + self.__y**2)


class Vecteur3D(Vecteur2D):
    def __init__(self, x = 0, y = 0, z = 0):
        super().__init__(x=0,y=0)
        self.__z = z

    def getZ(self):
        return self.__z

    def ToString(self):
        return " x : "+str(self.getX())+" y : "+str(self.getY())+" z : "+str(self.__z)

    def Equals(self , vec1):
        if self.getX() == vec.getX() and  self.__y == vec.getY() and self.__z == vec.getZ():
            return True
        else :
            return False

    def Norme(self):
        return math.sqrt(self.getX()**2 + self.getY()**2 + self.__z**2)


vec = Vecteur2D(10,15)
vec1 = Vecteur2D(10,15)
print(vec.ToString())
print(vec.Equals(vec1))
print(vec.Norme())



vec2 = Vecteur3D(10,15, 12)
vec3 = Vecteur3D(10,15, 12)
print(vec2.ToString())
print(vec2.Equals(vec3))
print(vec2.Norme())
print(vec2.getNbre())