from abc import ABC, abstractmethod

# Interfaz objetivo que el cliente espera usar
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, file_name: str) -> None:
        pass