package prototype;

public class Rectangle implements ShapePrototype{
    private String color;
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public ShapePrototype clone() {
        Rectangle clone = new Rectangle(this.width, this.height);
        clone.setColor(this.color);
        return clone;
    }

    @Override
    public void draw() {
        System.out.println("Dibujando rectángulo - Ancho: " + width
                + ", Alto: " + height + ", Color: " + color);
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
