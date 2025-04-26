from ShapeRegistry import ShapeRegistry
from Circle import Circle

# 4. Demo de uso
if __name__ == "__main__":
    # Obtener prototipos básicos
    circle1 = ShapeRegistry.get_shape("basic_circle")
    rectangle1 = ShapeRegistry.get_shape("basic_rectangle")

    # Personalizar prototipos
    circle1.set_color("Rojo")
    rectangle1.set_color("Azul")

    print("Formas originales:")
    circle1.draw()
    rectangle1.draw()

    # Clonar formas personalizadas
    circle2 = circle1.clone()
    rectangle2 = rectangle1.clone()

    # Modificar clones
    circle2.set_color("Verde")
    rectangle2.set_color("Amarillo")

    print("\nFormas clonadas modificadas:")
    circle2.draw()
    rectangle2.draw()

    print("\nFormas originales (no modificadas):")
    circle1.draw()
    rectangle1.draw()

    # Crear nuevo prototipo en tiempo de ejecución
    big_circle = Circle(50)
    big_circle.set_color("Morado")
    ShapeRegistry.add_prototype("big_circle", big_circle)

    new_big_circle = ShapeRegistry.get_shape("big_circle")
    print("\nNuevo prototipo registrado:")
    new_big_circle.draw()