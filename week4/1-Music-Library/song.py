class Song():

    def __init__(self, title="", artist="", album="", length=""):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        result = "{} - {} from {} - {}"
        return result.format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and \
            self.album == other.album and self.length == other.length

    def __hash__(self):
        return hash(self.__str__())

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict}

    def get_length(self, hours=False, minutes=False, seconds=False):
        result = self.length.split(":")
        if (seconds is True):
            if len(result) == 2:
                return int(int(result[0]) * 60 + int(result[1]))
            else:
                return int(int(result[0]) * 3600 + int(result[1]) * 60 +
                           int(result[2]))
        elif (minutes is True):
            if len(result) == 2:
                return int(result[0])
            else:
                return int(int(result[0]) * 60 + int(result[1]))
        elif (hours is True):
            if len(result) == 3:
                return int(result[0])
            else:
                return 0
        else:
            return str(self.length)

# my_song = Song(title="Odin", artist="Manowar",
               # album="The Sons of Odin", length="3:44")
# print(my_song.prepare_json())
