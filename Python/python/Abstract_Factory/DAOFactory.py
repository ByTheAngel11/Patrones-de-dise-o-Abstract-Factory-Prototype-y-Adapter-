from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from .UserDAO import UserDAO

# 1. Interfaz Abstract Factory
class DAOFactory(ABC):
    @abstractmethod
    def create_user_dao(self) -> UserDAO:
        pass

# 2. Factory concreta para SQL
class SQLDAOFactory(DAOFactory):
    def create_user_dao(self) -> UserDAO:
        from .SQLUserDAO import SQLUserDAO
        return SQLUserDAO()