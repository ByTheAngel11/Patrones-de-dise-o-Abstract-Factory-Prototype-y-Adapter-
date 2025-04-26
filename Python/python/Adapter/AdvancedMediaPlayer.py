from abc import ABC, abstractmethod

# Interfaz incompatible que necesita ser adaptada
class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def play_vlc(self, file_name: str) -> None:
        pass

    @abstractmethod
    def play_mp4(self, file_name: str) -> None:
        pass