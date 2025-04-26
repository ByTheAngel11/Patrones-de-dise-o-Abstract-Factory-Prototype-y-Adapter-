package abstract_Factory;

import java.util.List;

public class AbstractFactoryDemo {
    public static void main(String[] args) {
        // 1. Crear la fábrica concreta
        DAOFactory factory = new SQLDAOFactory();

        // 2. Crear el objeto de negocio con la fábrica
        BusinessObject businessObject = new BusinessObject(factory);

        // 3. Obtener y mostrar los usuarios
        List<TransferObject> users = businessObject.getAllUsers();

        System.out.println("Lista de usuarios:");
        users.forEach(user ->
                System.out.println(" - " + user.getUserData())
        );
    }
}