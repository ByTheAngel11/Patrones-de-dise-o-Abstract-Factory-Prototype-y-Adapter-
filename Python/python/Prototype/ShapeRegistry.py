from .Circle import Circle
from .Rectangle import Rectangle
from .ShapePrototype import ShapePrototype

# 3. Registro de prototipos
class ShapeRegistry:
    _prototypes = {
        "basic_circle": Circle(10),
        "basic_rectangle": Rectangle(20, 15)
    }

    @classmethod
    def get_shape(cls, shape_name: str) -> ShapePrototype:
        prototype = cls._prototypes.get(shape_name)
        if prototype:
            return prototype.clone()
        raise ValueError(f"Prototipo no registrado: {shape_name}")

    @classmethod
    def add_prototype(cls, name: str, prototype: ShapePrototype):
        cls._prototypes[name] = prototype