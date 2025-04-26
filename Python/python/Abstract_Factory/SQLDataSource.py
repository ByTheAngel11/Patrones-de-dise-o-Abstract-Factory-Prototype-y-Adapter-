from typing import List

# 7. Fuente de datos simulada
class SQLDataSource:
    def get_data(self) -> List[str]:
        # Simular acceso a base de datos
        return ["User1", "User2", "User3"]