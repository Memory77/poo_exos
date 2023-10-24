import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        lowleft = rectangle.lowleft
        upright = rectangle.upright
        # lowleft et upright sont les coordonnées du coin
        # en bas à gauche et en haut à droite du rectangle
        if lowleft.x < self.x < upright.x\
                and lowleft.y < self.y < upright.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        x = point.x
        y = point.y
        return ((self.x - x)**2 + (self.y - y)**2)**(1/2)

class Rectangle:

    def __init__(self, lowleft, upright): # Qu'est-ce que lowleft et upright ? Des points !
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        #l'air c'est longueur * largeur
        longueur = self.upright.y - self.lowleft.y
        print(f"la longueur est {longueur}")
        largeur = self.upright.x - self.lowleft.x
        print(f"la largeur est {largeur}")
        aire = longueur * largeur
        return [longueur, largeur, aire]
    

point1 = Point(random.randint(1,4),random.randint(1,4))
point2 = Point(random.randint(5,9),random.randint(5,9))

rectangle = Rectangle(point1, point2)