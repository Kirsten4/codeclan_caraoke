import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Kirsten",30,"Street Spirit",23.50)

    def test_guest_has_name(self):
        self.assertEqual("Kirsten", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(30, self.guest.age)

    def test_guest_has_favourtie_song(self):
        self.assertEqual("Street Spirit", self.guest.favourite_song)

    def test_guest_has_money_in_wallet(self):
        self.assertEqual(23.50, self.guest.money_in_wallet)

    def test_pay_tab(self):
        self.guest.pay_tab(4.00)
        self.assertEqual(19.50, self.guest.money_in_wallet)

    def test_cheer_favourite_song__song_is_favourite(self):
        song = Song("Street Spirit", "Radiohead", 4.19)
        self.assertEqual("Whoo!", self.guest.cheer_favourite_song(song))

    def test_cheer_favourite_song__song_is_not_favourite(self):
        song = Song("Where is my mind?", "Pixies", 3.37)
        self.assertEqual(None, self.guest.cheer_favourite_song(song))
