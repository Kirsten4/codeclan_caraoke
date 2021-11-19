class Room:
    
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
        self.guests_in_room = []
        self.playlist = []

    def check_in_guest(self,guest):
        self.guests_in_room.append(guest)

    def check_out_guest(self,guest):
        self.guests_in_room.remove(guest)

    def add_song_to_playlist(self,song):
        self.playlist.append(song)

    
