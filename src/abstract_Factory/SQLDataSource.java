package abstract_Factory;

import java.util.Arrays;
import java.util.List;

public class SQLDataSource {
    public List<String> getData() {
        // Simulación de datos obtenidos de una base de datos
        return Arrays.asList("User1", "User2", "User3");
    }
}