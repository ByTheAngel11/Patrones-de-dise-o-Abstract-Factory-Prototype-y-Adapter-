package prototype;

public class PrototypePatternDemo {
    public static void main(String[] args) {
        // Obtener prototipos básicos
        ShapePrototype circle1 = ShapeRegistry.getShape("basic_circle");
        ShapePrototype rectangle1 = ShapeRegistry.getShape("basic_rectangle");

        // Personalizar prototipos
        circle1.setColor("Rojo");
        rectangle1.setColor("Azul");

        System.out.println("Formas originales:");
        circle1.draw();
        rectangle1.draw();

        // Clonar formas personalizadas
        ShapePrototype circle2 = circle1.clone();
        ShapePrototype rectangle2 = rectangle1.clone();

        // Modificar clones
        circle2.setColor("Verde");
        rectangle2.setColor("Amarillo");

        System.out.println("\nFormas clonadas modificadas:");
        circle2.draw();
        rectangle2.draw();

        System.out.println("\nFormas originales (no modificadas):");
        circle1.draw();
        rectangle1.draw();

        // Crear nuevo prototipo en tiempo de ejecución
        ShapePrototype bigCircle = new Circle(50);
        bigCircle.setColor("Morado");
        ShapeRegistry.addPrototype("big_circle", bigCircle);

        ShapePrototype newBigCircle = ShapeRegistry.getShape("big_circle");
        System.out.println("\nNuevo prototipo registrado:");
        newBigCircle.draw();
    }
}
