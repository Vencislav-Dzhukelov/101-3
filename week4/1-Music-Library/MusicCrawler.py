import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from song import Song
from playlist import Playlist
import datetime


class MusicCrawler:

    def __init__(self, path):
        self.path = path
        self.files_in_dir = [x for x in os.listdir(path) if x.endswith('.mp3')]

    def generate_playlist(self):
        party_animal_songs = Playlist(name="Party Animal")
        for music_file in self.files_in_dir:
            audio = MP3(self.path + music_file, ID3=EasyID3)
            artist = audio['artist'][0]
            title = audio['title'][0]
            album = audio['album'][0]
            length = str(datetime.timedelta(seconds=int(audio.info.length)))
            new_song = Song(
                title=title, artist=artist, album=album, length=length)
            new_song.path = music_file
            party_animal_songs.add_song(new_song)
        return party_animal_songs
