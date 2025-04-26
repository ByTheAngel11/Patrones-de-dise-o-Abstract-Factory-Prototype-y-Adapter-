package adapter;

public class VlcPlayer implements AdvancedMediaPlayer{
    @Override
    public void playVlc(String fileName) {
        System.out.println("Reproduciendo archivo VLC: " + fileName);
    }

    @Override
    public void playMp4(String fileName) {
        // No hace nada
    }
}
