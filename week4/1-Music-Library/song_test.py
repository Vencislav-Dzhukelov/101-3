from song import Song
import unittest


class TestSong(unittest.TestCase):

    def setUp(self):
        self.my_song = Song(title="Odin", artist="Manowar",
                            album="The Sons of Odin", length="3:44")

    def test_init(self):
        self.assertTrue(isinstance(self.my_song, Song))
        self.assertEqual(self.my_song.title, "Odin")
        self.assertEqual(self.my_song.artist, "Manowar")
        self.assertEqual(self.my_song.album, "The Sons of Odin")
        self.assertEqual(self.my_song.length, "3:44")

    def test_str(self):
        result = "Manowar - Odin from The Sons of Odin - 3:44"
        self.assertEqual(str(self.my_song), result)

    def test_eq(self):
        his_song = Song(title="Odin", artist="Manowar",
                        album="The Sons of Odin", length="3:44")
        self.assertTrue(his_song == self.my_song)

    def test_hash(self):
        self.assertIsNotNone(hash(self.my_song))

    def test_length(self):
        self.assertEqual(self.my_song.get_length(seconds=True), 224)
        self.assertEqual(self.my_song.get_length(minutes=True), 3)

if __name__ == '__main__':
    unittest.main()
