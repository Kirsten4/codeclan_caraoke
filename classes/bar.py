class Bar:

    def __init__(self,menu):
        self.menu = menu

    def add_drink_to_tab(self,room,guest,drink):
        room.bar_tab[guest] += drink
        