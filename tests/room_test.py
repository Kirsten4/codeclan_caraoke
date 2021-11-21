import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Pop Room", 3)
        self.guest_1 = Guest("Kirsten",30,"Street Spirit",23.50)
        self.guest_2 = Guest("David",29,"Where is my mind?",16.00)
        self.guest_3 = Guest("Steven",30,"Under the sea",45.50)
        self.guest_4 = Guest("Gordon",31,"I want it that way",34.00)
        self.guest_5 = Guest("Allan",60,"Non, Je ne regrette rien",3.50)
        self.song = Song("Street Spirit", "Radiohead", 4.19)

    def test_room_has_name(self):
        self.assertEqual("Pop Room", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room.capacity)

    def test_room_has_empty_list_of_guests(self):
        self.assertEqual([], self.room.guests_in_room)

    def test_room_has_empty_playlist(self):
        self.assertEqual([], self.room.playlist)

    def test_room_has_entry_fee(self):
        self.assertEqual(6.00,self.room.entry_fee)

    def test_available_room_capacity__space_available(self):
        self.room.guests_in_room.append(self.guest_1)
        self.assertEqual(True, self.room.available_room_capacity())

    def test_available_room_capacity__room_full(self):
        self.room.guests_in_room.append(self.guest_1)
        self.room.guests_in_room.append(self.guest_2)
        self.room.guests_in_room.append(self.guest_3)
        self.assertEqual(False, self.room.available_room_capacity())
    
    def test_guest_can_pay__yes(self):
        self.assertEqual(True, self.room.guest_can_pay(self.guest_1))

    def test_guest_can_pay__no(self):
        self.assertEqual(False, self.room.guest_can_pay(self.guest_5))

    def test_check_in_guest__yes(self):
        self.room.check_in_guest(self.guest_1)
        self.assertIn(self.guest_1, self.room.guests_in_room)

    def test_check_in_guest__no_too_full(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.assertEqual("No entry", self.room.check_in_guest(self.guest_4))   

    def test_check_in_guest__no_cannot_afford(self):
        self.assertEqual("No entry", self.room.check_in_guest(self.guest_5))     

    def test_check_out_guest(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.assertNotIn(self.guest_1, self.room.guests_in_room)

    def test_add_song_to_playlist(self):
         self.room.add_song_to_playlist(self.song)
         self.assertIn(self.song, self.room.playlist)   

