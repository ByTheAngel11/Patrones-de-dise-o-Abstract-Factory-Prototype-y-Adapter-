from AudioPlayer import AudioPlayer

# Demo de uso del patrón
if __name__ == "__main__":
    audio_player = AudioPlayer()

    audio_player.play("mp3", "cancion.mp3")
    audio_player.play("mp4", "video.mp4")
    audio_player.play("vlc", "pelicula.vlc")
    audio_player.play("avi", "pelicula.avi")