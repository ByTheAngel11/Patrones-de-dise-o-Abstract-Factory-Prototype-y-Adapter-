package abstract_Factory;

import java.util.List;
import java.util.stream.Collectors;


public class SQLUserDAO implements UserDAO{
    private SQLDataSource dataSource = new SQLDataSource();

    @Override
    public List<TransferObject> getUsers() {
        List<String> rawData = dataSource.getData();
        return rawData.stream()
                .map(TransferObject::new)
                .collect(Collectors.toList());
    }
}
