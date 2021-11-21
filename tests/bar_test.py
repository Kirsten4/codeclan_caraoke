import unittest
from classes.bar import Bar
from classes.guest import Guest
from classes.room import Room

class TestBar(unittest.TestCase):
    
    def setUp(self):
        self.bar = Bar({"vodka":3.00, "beer":4.50, "coke":2.50 })

    def test_bar_has_menu(self):
        self.assertEqual({"vodka":3.00, "beer":4.50, "coke":2.50 }, self.bar.menu)

    def test_add_drink_to_tab__entry_fee_plus_drink(self):
        guest_1 = Guest("Kirsten",30,"Street Spirit",23.50)
        room = Room("Pop Room", 3, 6.00, 100.00)
        room.check_in_guest(guest_1)
        self.assertEqual({guest_1:6.00}, room.bar_tab)
        self.bar.add_drink_to_tab(room,guest_1,self.bar.menu["coke"])
        self.assertEqual({guest_1:8.50}, room.bar_tab)

    def test_add_drink_to_tab__multiple_guests_and_drinks(self):
        guest_1 = Guest("Kirsten",30,"Street Spirit",23.50)
        guest_2 = Guest("David",29,"Where is my mind?",16.00)
        room = Room("Pop Room", 3, 6.00, 100.00)
        room.check_in_guest(guest_1)
        room.check_in_guest(guest_2)
        self.bar.add_drink_to_tab(room,guest_1,self.bar.menu["coke"])
        self.bar.add_drink_to_tab(room,guest_1,self.bar.menu["vodka"])
        self.bar.add_drink_to_tab(room,guest_2,self.bar.menu["beer"])
        self.bar.add_drink_to_tab(room,guest_2,self.bar.menu["beer"])
        self.assertEqual({guest_1:11.50, guest_2:15.00}, room.bar_tab)