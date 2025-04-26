from .AdvancedMediaPlayer import AdvancedMediaPlayer

# Implementación concreta para MP4
class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name: str) -> None:
        pass  # No implementado

    def play_mp4(self, file_name: str) -> None:
        print(f"Reproduciendo archivo MP4: {file_name}")