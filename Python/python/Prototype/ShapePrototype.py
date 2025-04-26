from abc import ABC, abstractmethod

# 1. Interfaz del Prototipo
class ShapePrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def set_color(self, color: str):
        pass

    @property
    @abstractmethod
    def color(self) -> str:
        pass