class House:
    def __init__(self, wall_area) -> None:
        self.wall_area = wall_area



class Paint:
    def __init__(self, buckets, color) -> None:
        self.buckets = buckets
        self.color = color

    def prix_total(self):
        if self.color == "blanche":
            prix = self.buckets * 1.99
            return prix
        else:
            prix = self.buckets * 2.19
            return prix

a = Paint(2, "blanche")
print(a.prix_total())