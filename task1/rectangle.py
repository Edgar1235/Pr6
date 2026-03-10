class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height) / 2

    def perimeter(self):
        # приблизний периметр (для прикладу)
        return self.width + self.height + (self.width**2 + self.height**2) ** 0.5
triangle1 = Triangle(6, 4)
triangle2 = Triangle(8, 5)
print("Площа трикутника 1:", triangle1.area())
print("Периметр трикутника 1:", triangle1.perimeter())
print("Площа трикутника 2:", triangle2.area())
print("Периметр трикутника 2:", triangle2.perimeter())