class Guest:
    
    def __init__(self,name,age,favourite_song,money_in_wallet):
        self.name = name
        self.age = age
        self.favourite_song = favourite_song
        self.money_in_wallet = money_in_wallet

    def pay_tab(self,tab):
        self.money_in_wallet -= tab

    def cheer_favourite_song(self,song):
        if song.name == self.favourite_song:
            return "Whoo!"