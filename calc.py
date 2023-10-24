class Calculatrice:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    
    def addition(self):
        resultat = self.a + self.b
        return resultat
    
    def soustraction(self):
        resultat = self.a - self.b
        return resultat
    
    def multiplication(self):
        resultat = self.a * self.b
        return resultat
    
    def division(self):
        if self.b == 0:
            print("on ne peut pas diviser par 0")
        else:
            resultat = self.a / self.b
        return resultat


chiffres = Calculatrice(4,5)
print(chiffres.a)
print(chiffres.b)

print(Calculatrice.division(chiffres))
print(Calculatrice.multiplication(chiffres))
print(Calculatrice.addition(chiffres))


