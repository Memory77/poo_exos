


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
    


num1 = int(input("saisir un premier chiffre : "))
operation = input("saisir une operation : ")
num2 = int(input("saisir un deuxieme chiffre : "))

#initialiser un objet de la class calc
calculette = Calc()
resultat = calculette.operation(operation,num1,num2)
print(resultat)