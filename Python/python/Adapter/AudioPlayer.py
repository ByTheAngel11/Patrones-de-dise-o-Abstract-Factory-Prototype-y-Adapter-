from .MediaPlayer import MediaPlayer
from .MediaAdapter import MediaAdapter

# Implementación concreta que usa el Adapter
class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.media_adapter = None

    def play(self, audio_type: str, file_name: str) -> None:
        # Soporte nativo para mp3
        if audio_type.lower() == "mp3":
            print(f"Reproduciendo archivo MP3: {file_name}")
        # Usar adapter para otros formatos
        elif audio_type.lower() in ("vlc", "mp4"):
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, file_name)
        else:
            print(f"Formato no soportado: {audio_type}")