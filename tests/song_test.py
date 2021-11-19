import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Street Spirit", "Radiohead", 4.19)

    def test_song_has_name(self):
        self.assertEqual("Street Spirit", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Radiohead", self.song.artist)

    def test_song_has_duration(self):
        self.assertEqual(4.19, self.song.duration)