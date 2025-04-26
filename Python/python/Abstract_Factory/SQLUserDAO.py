from __future__ import annotations
from typing import List
from .UserDAO import UserDAO
from .TransferObject import TransferObject
from .SQLDataSource import SQLDataSource

# 4. Implementación concreta del Producto
class SQLUserDAO(UserDAO):
    def __init__(self):
        self.data_source = SQLDataSource()

    def get_users(self) -> List[TransferObject]:
        raw_data = self.data_source.get_data()
        return [TransferObject(data) for data in raw_data]