package abstract_Factory;

public class SQLDAOFactory implements DAOFactory {
    @Override
    public UserDAO createUserDAO() {
        return new SQLUserDAO();
    }
}
