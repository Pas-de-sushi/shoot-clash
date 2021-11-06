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

    def limit(self, x: float = None, y: float = None):
        """
        Limite le vecteur à un maximum de x et y.
        Si la limite vaut None, alors la limite n'est pas appliquée.
        """
        if x != None:
            if self.x > x:
                self.x = x
            elif self.x < -x:
                self.x = -x

        if y != None:
            if self.y > y:
                self.y = y
            elif self.y < -y:
                self.y = -y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vector":
        return Vector(self.x * other, self.y * other)
