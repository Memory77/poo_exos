# Exercice : Héritage
# L'atelier de peinture décide qu'il est judicieux d'appliquer des remises sur la peinture pour des occasions spéciales. 
# Par conséquent, votre nouvelle tâche en tant que programmeur est d'incorporer un nouveau type d'objet - DiscountedPaint. 

# Votre tâche exacte consiste à :

# 1. Créer une classe DiscountedPaint sous le code existant. Cette classe doit hériter de Paint.

# 2. Ajouter une méthode discounted_price à cette classe. La méthode doit avoir un paramètre discount_percentage. 
# Il n'est pas nécessaire de créer une méthode __init__.

# 3. La méthode discounted_price doit calculer et renvoyer un prix actualisé basé sur la sortie de self.total_price() et la 
# valeur de discount_percentage. Vous pourriez faire cela en calculant d'abord le prix total, puis la remise totale, 
# puis en soustrayant la remise totale du prix total pour obtenir le prix escompté et le renvoyer.


class Paint:

    def __init__(self, buckets, color): # Or get house area and height
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19
            
class DiscountedPaint(Paint):

    def discounted_price(self,discount_percentage):
        remise = 1 - (discount_percentage/100) #une remise donc on veut diminuer de 35% le prix 
        nouveau_prix = self.total_price() * remise
        return nouveau_prix

paint = Paint(10,"white")
prix = paint.total_price()
print(prix)

nouveauprix = DiscountedPaint.discounted_price(paint, 35)
print(nouveauprix)