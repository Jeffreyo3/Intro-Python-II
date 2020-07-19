# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.avaliableItems = []
    
    def __str__(self):
        return f"\n{self.name}, {self.description}"

    def add_item(self, item):
        self.avaliableItems.append(item)

    def remove_item(self, item):
        self.avaliableItems.remove(item)

    def print_items(self):
        itemcount = self.avaliableItems.__len__();
        if (itemcount == 0):
            print("There are no items left in this room.")
        else:
            for item in self.avaliableItems:
                print(item)