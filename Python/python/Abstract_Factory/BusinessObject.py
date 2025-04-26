from __future__ import annotations
from typing import List
from .DAOFactory import DAOFactory
from .TransferObject import TransferObject

# 5. Clase de negocio que utiliza el patrón
class BusinessObject:
    def __init__(self, factory: DAOFactory):
        self.factory = factory

    def get_all_users(self) -> List[TransferObject]:
        user_dao = self.factory.create_user_dao()
        return user_dao.get_users()