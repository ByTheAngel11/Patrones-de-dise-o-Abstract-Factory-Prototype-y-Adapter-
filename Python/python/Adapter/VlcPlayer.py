from .AdvancedMediaPlayer import AdvancedMediaPlayer

# Implementación concreta para VLC
class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str) -> None:
        print(f"Reproduciendo archivo VLC: {file_name}")

    def play_mp4(self, file_name: str) -> None:
        pass  # No implementado