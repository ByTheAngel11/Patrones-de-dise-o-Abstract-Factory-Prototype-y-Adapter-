package prototype;

public interface ShapePrototype extends Cloneable {
    ShapePrototype clone();
    void draw();
    void setColor(String color);
    String getColor();
}
