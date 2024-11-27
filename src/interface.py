

class MediaPlayer:
    """_summary_
    """

    def play(self):
        raise NotImplementedError


class AudioPlayer(MediaPlayer):

    def play(self, audio_type, file_name):
        if audio_type == "mp3":
            print(f"Воспроизведение mp3-файла: {file_name}")
        else:
            print(f"Тип аудио {audio_type} не поддерживается.")
