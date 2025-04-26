package abstract_Factory;

import java.util.List;

public class BusinessObject {
    private DAOFactory factory;

    public BusinessObject(DAOFactory factory) {
        this.factory = factory;
    }

    public List<TransferObject> getAllUsers() {
        UserDAO userDAO = factory.createUserDAO();
        return userDAO.getUsers();
    }
}