import copy
from .ShapePrototype import ShapePrototype

# Implementación concreta del prototipo: Círculo
class Circle(ShapePrototype):
    def __init__(self, radius: int):
        self._radius = radius
        self._color = None

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        print(f"Dibujando círculo - Radio: {self._radius}, Color: {self._color}")

    def set_color(self, color: str):
        self._color = color

    @property
    def color(self):
        return self._color