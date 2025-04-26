import copy
from .ShapePrototype import ShapePrototype

# Implementación concreta del prototipo: Rectángulo
class Rectangle(ShapePrototype):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._color = None

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        print(f"Dibujando rectángulo - Ancho: {self._width}, Alto: {self._height}, Color: {self._color}")

    def set_color(self, color: str):
        self._color = color

    @property
    def color(self):
        return self._color