from adapter import (
    VlcAdapter,
    VlcPlayer)

from interface import AudioPlayer


def client_code():
    audio_player = AudioPlayer()
    audio_player.play("mp3", "song.mp3")

    vlc_player = VlcPlayer()
    vlc_adapter = VlcAdapter(vlc_player)
    vlc_adapter.play("vlc", "movie.vlc")
    vlc_adapter.play("mp4", "video.mp4")  


client_code()