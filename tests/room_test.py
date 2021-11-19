import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Pop Room", 8)
        self.guest = Guest("Kirsten",30,"Street Spirit")
        self.song = Song("Street Spirit", "Radiohead", 4.19)

    def test_room_has_name(self):
        self.assertEqual("Pop Room", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.room.capacity)

    def test_room_has_list_of_guests(self):
        self.assertEqual([], self.room.guests_in_room)

    def test_room_has_playlist(self):
        self.assertEqual([], self.room.playlist)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertIn(self.guest, self.room.guests_in_room)

    def test_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertNotIn(self.guest, self.room.guests_in_room)

    def test_add_song_to_playlist(self):
         self.room.add_song_to_playlist(self.song)
         self.assertIn(self.song, self.room.playlist)   