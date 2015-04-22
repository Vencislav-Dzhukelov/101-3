from playlist import Playlist
from song import Song
import unittest


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.my_playlist = Playlist("Name")
        self.song1 = Song(title="Odin", artist="Manowar",
                          album="The Sons of Odin", length="3:44")
        self.song2 = Song(title="Odin2", artist="Manowar",
                          album="The Sons of Odins", length="13:44")

    def test_init(self):
        self.assertTrue(isinstance(self.my_playlist, Playlist))

    def test_add_song(self):
        self.my_playlist.add_song(self.song1)
        self.assertIn(self.song1, self.my_playlist.playlist)

    def test_remove_song(self):
        self.my_playlist.add_song(self.song1)
        self.my_playlist.add_song(self.song2)
        self.my_playlist.remove_song(self.song1)
        self.assertNotIn(self.song1, self.my_playlist.playlist)
        self.assertIn(self.song2, self.my_playlist.playlist)

    def test_add_songs(self):
        self.my_playlist.add_song(self.song1)
        my_song = Song(title="Odin3", artist="Manowarr",
                       album="The Sons of Odins", length="1:44")
        lst = [self.song2, my_song]
        self.my_playlist.add_songs(lst)
        self.assertIn(self.song1, self.my_playlist.playlist)
        self.assertIn(self.song2, self.my_playlist.playlist)
        self.assertIn(my_song, self.my_playlist.playlist)

    def test_total_length(self):
        self.my_playlist.add_song(self.song1)
        self.my_playlist.add_song(self.song2)
        self.assertEqual(self.my_playlist.total_length(), "00:17:28")

    def test_next_song(self):
        self.my_playlist.add_song(self.song1)
        self.my_playlist.add_song(self.song2)
        self.assertEqual(self.my_playlist.next_song(), self.song1)


if __name__ == '__main__':
    unittest.main()
