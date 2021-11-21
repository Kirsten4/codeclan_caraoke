class Room:
    
    def __init__(self,name,capacity,entry_fee,till_value):
        self.name = name
        self.capacity = capacity
        self.guests_in_room = []
        self.playlist = []
        self.entry_fee = entry_fee
        self.till_value = till_value
        self.bar_tab = {}
      

    def available_room_capacity(self):
        return self.capacity > len(self.guests_in_room)

    def guest_can_pay(self,guest):
        return guest.money_in_wallet >= self.entry_fee
    
    def check_in_guest(self,guest):
        if self.available_room_capacity() and self.guest_can_pay(guest):
            self.guests_in_room.append(guest)
            self.bar_tab[guest] = self.entry_fee
        else:
            return "No entry"

    def check_out_guest(self,guest):
        self.guests_in_room.remove(guest)
        guest.pay_tab(self.bar_tab[guest])
        self.till_value += self.bar_tab[guest]

    def add_song_to_playlist(self,song):
        self.playlist.append(song)

    def favourite_song_in_playlist(self,guest):
        message = "Song not found"
        for song in self.playlist:
            if guest.cheer_favourite_song(song) != None:
                message = guest.cheer_favourite_song(song)
        return message
