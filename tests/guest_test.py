import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Kirsten",30,"Street Spirit",23.50)

    def test_guest_has_name(self):
        self.assertEqual("Kirsten", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(30, self.guest.age)

    def test_guest_has_favourtie_song(self):
        self.assertEqual("Street Spirit", self.guest.favourite_song)

    def test_guest_has_wallet(self):
        self.assertEqual(23.50, self.guest.money_in_wallet)
        