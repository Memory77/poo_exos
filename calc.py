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





#deuxieme methode
class Calc:
    def operation(self, operation, a, b):
        if operation == "+":
            self.a = a
            self.b = b
            resultat = self.a + self.b
            result = f"Le resultat de {self.a} + {self.b} est {resultat}"
            return result
        elif operation == "*":
            self.a = a
            self.b = b
            resultat = self.a * self.b
            result = f"Le resultat de {self.a} * {self.b} est {resultat}"
            return result
        elif operation == "-":
            self.a = a
            self.b = b
            resultat = self.a - self.b
            result = f"Le resultat de {self.a} - {self.b} est {resultat}"
            return result
        elif operation == "/":
            if b == 0:
                print("On ne peut pas diviser par 0")
            else:
                self.a = a
                self.b = b
                resultat = self.a / self.b
                result = f"Le resultat de {self.a} - {self.b} est {resultat}"
                return result
        else:
            print("resultat invalide")
    



#initialiser un objet de la class calc
calculette = Calc()
resultat = calculette.operation("*",1,5)
print(resultat)