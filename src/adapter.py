from adaptable_class import VlcPlayer
from interface import MediaPlayer


class VlcAdapter(MediaPlayer):

    def __init__(self, vlc_player: VlcPlayer):
        self.vlc_player = vlc_player

    def play(self, audio_type, file_name):
        if audio_type == "vlc":
            self.vlc_player.play_vlc(file_name)
        else:
            print(f"Тип аудио {audio_type} не поддерживается.")
