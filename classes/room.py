class Room:
    
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
        self.guests_in_room = []
        self.playlist = []
        self.entry_fee = 6.00

    def available_room_capacity(self):
        return self.capacity > len(self.guests_in_room)

    def guest_can_pay(self,guest):
        return guest.money_in_wallet >= self.entry_fee
    
    def check_in_guest(self,guest):
        if self.available_room_capacity() and self.guest_can_pay(guest):
            self.guests_in_room.append(guest)
        else:
            return "No entry"

    def check_out_guest(self,guest):
        self.guests_in_room.remove(guest)

    def add_song_to_playlist(self,song):
        self.playlist.append(song)

    
