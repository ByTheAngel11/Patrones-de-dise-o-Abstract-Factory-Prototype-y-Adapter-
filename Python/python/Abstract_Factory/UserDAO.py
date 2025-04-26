from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from .TransferObject import TransferObject

# 3. Interfaz para el Producto
class UserDAO(ABC):
    @abstractmethod
    def get_users(self) -> List[TransferObject]:
        pass