# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def __str__(self):
        return f"{self.name} has moved to: {self.room}"

    def pickup(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
        # maybe consider inventory max??

    def print_items(self):
        itemcount = self.inventory.__len__();
        if (itemcount == 0):
            print("You have no items in your baggy :'(")
        else:
            for item in self.inventory:
                print(item)