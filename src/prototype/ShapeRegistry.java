package prototype;

import java.util.HashMap;
import java.util.Map;

public class ShapeRegistry {
    private static Map<String, ShapePrototype> prototypes = new HashMap<>();

    static {
        // Prototipos iniciales
        prototypes.put("basic_circle", new Circle(10));
        prototypes.put("basic_rectangle", new Rectangle(20, 15));
    }

    public static ShapePrototype getShape(String type) {
        return prototypes.get(type).clone();
    }

    public static void addPrototype(String key, ShapePrototype prototype) {
        prototypes.put(key, prototype);
    }
}
