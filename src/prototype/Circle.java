package prototype;

public class Circle implements ShapePrototype{
    private String color;
    private int radius;

    public Circle(int radius) {
        this.radius = radius;
    }

    @Override
    public ShapePrototype clone() {
        Circle clone = new Circle(this.radius);
        clone.setColor(this.color);
        return clone;
    }

    @Override
    public void draw() {
        System.out.println("Dibujando círculo - Radio: " + radius
                + ", Color: " + color);
    }

    @Override
    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String getColor() {
        return color;
    }
}
