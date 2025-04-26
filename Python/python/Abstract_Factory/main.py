from DAOFactory import SQLDAOFactory
from BusinessObject import BusinessObject

# Ejemplo de uso
if __name__ == "__main__":
    sql_factory = SQLDAOFactory()
    business_object = BusinessObject(sql_factory)

    users = business_object.get_all_users()
    for user in users:
        print(user.user_data)