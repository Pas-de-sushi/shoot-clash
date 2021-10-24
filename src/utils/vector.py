class Vector:
    """
    Classe représentant un vecteur.

    Opérations supportés :
    - Addition et soustraction avec un autre vecteur
    - Multiplication avec un nombre
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vector":
        return Vector(self.x * other, self.y * other)
