from song import Song
from tabulate import tabulate
import time
import random
import json


class Playlist():

    def __init__(self, name, repeat=False, shuffle=False):
        self.playlist = []
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.__current_song_index = 0
        self.__shuffle_played_songs = set()

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        result = 0
        for item in self.playlist:
            result = result + int(item.get_length(seconds=True))
        return time.strftime('%H:%M:%S', time.gmtime(result))

    def artists(self):
        lst = []
        for item in self.playlist:
            lst.append(item.artist)
        result = dict((i, lst.count(i)) for i in lst)
        return result

    def pprint_playlist(self):
        result = []
        headers = ["Artist", "Song", "Length"]
        for item in self.playlist:
            temp = [item.artist, item.title, item.length]
            result.append(temp)

        print (tabulate(result, headers=headers))

    def has_next_song(self):
        return self.__current_song_index < len(self.playlist)

    def __shuffle(self):
        song = random.choice(self.playlist)

        while song in self.__shuffle_played_songs:
            song = random.choice(self.playlist)

        self.__shuffle_played_songs.add(song)

        if len(self.__shuffle_played_songs) == len(self.playlist):
            self.__shuffle_played_songs = set()

        return song

    def next_song(self):
        if self.shuffle:
            return self.__shuffle()

        if not self.has_next_song() and self.repeat == "False":
            raise Exception("End of playlist")

        if not self.has_next_song() and self.repeat == "True":
            self.__current_song_index = 0

        song = self.playlist[self.__current_song_index]
        self.__current_song_index += 1

        return song

    def prepare_json(self):
        data = {
            "name": self.name,
            "songs": [song.prepare_json() for song in self.playlist]
        }

        return data

    def save(self, indent=True):
        filename = self.name.replace(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song["title"], album=dict_song["album"], length=dict_song["length"])
                p.add_song(song)

            return p

"""
my_playlist = Playlist("Name")
s1 = Song(title="Odin", artist="Manowar",
          album="The Sons of Odin", length="32:44")
s2 = Song(title="Odin", artist="Manowar1",
          album="The Sons of Odin", length="3:24")
s3 = Song(title="Odin", artist="Manowar",
          album="The Sons of Odin", length="3:44")
my_playlist.add_song(s1)
my_playlist.add_song(s2)
my_playlist.add_song(s3)
print (my_playlist.total_length())
print (my_playlist.artists())
my_playlist.pprint_playlist()
"""
