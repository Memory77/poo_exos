class ItemBibliothèque:
    def __init__(self, titre, date_publication):
        self.titre = titre
        self.date_publication = date_publication

    def description(self):
        return f"Titre: {self.titre}, Date de publication: {self.date_publication}"

class Livre(ItemBibliothèque):
    def __init__(self, titre, date_publication, auteur, ISBN):
        ItemBibliothèque.__init__(self, titre, date_publication)
        self.auteur = auteur
        self.ISBN = ISBN

    def description(self):  # Cette méthode surcharge la méthode parente
        base_desc = super().description()  # Utilise la méthode 'description' de la classe parente
        return f"{base_desc}, Auteur: {self.auteur}, ISBN: {self.ISBN}"

class Magazine(ItemBibliothèque):
    def __init__(self, titre, date_publication, editeur, numero_edition):
        ItemBibliothèque.__init__(self, titre, date_publication)
        self.editeur = editeur
        self.numero_edition = numero_edition

    def description(self):  # Cette méthode surcharge aussi la méthode parente
        base_desc = super().description()  # Utilise la méthode 'description' de la classe parente
        return f"{base_desc}, Éditeur: {self.editeur}, Édition: {self.numero_edition}"
    


items = [Livre("L'Étranger", "1942", "Albert Camus", "123456789"),
         Magazine("ScienceActu", "2022", "Éditions Sci", "42")]

for item in items:
    print(item.description())  # Le polymorphisme en action!
