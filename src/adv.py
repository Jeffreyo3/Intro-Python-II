from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all the items

item = {
    'sword': Item("Sword", "A basic chunk of sharp metal."),
    'potion': Item("Potion", "A bottle with mysterious blue liquid (not milk)."),
    'bomb': Item("Bomb", "It goes BOOOOOOOOoooooom!"),
    'key': Item("Key", "Usually is able to unlock things, but not always."),
    'trash': Item("Trash", "An unequipable non-tradeable item. Only good for dropping."),
    'treasure': Item("Treasure", "I think this is what you came here for?"),
    'shield': Item("Shield", "For blocking or wearing on your back if you're a turtle."),
    'food': Item("Food", "Intended for eating, but its a little moldy.")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
# room['foyer'] = {
#   s.to: room['outside'],
#   n_to: room['overlook'],
#   e_to: room['narrow']
# }
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Assign items to rooms

room['outside'].add_item(item['trash'])
room['foyer'].add_item(item['sword'])
room['foyer'].add_item(item['potion'])
room['overlook'].add_item(item['bomb'])
room['overlook'].add_item(item['key'])
room['overlook'].add_item(item['treasure'])
room['narrow'].add_item(item['trash'])
room['narrow'].add_item(item['shield'])
room['narrow'].add_item(item['food'])
room['treasure'].add_item(item['trash'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Jeff", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error movementMessage if the movement isn't allowed.
#
# If the user enters "q", quit the game.

menuMessage = f'Select a menu:\nM - Move\nI - Items\npress "Q" to exit.\n >> '
breaktext = "===---===---===---===---==="
print(breaktext)
menuInput = input(menuMessage)
print(breaktext)

while(menuInput.lower() != 'q'):
    while (menuInput.lower() == 'm'):
        movementMessage = f'Input a movement direction\nN - North\nS - South\nE - East\nW - West\nselect "C" to see current room\npress "Q" to exit.\n >> '
        movementInput = input(movementMessage)
        command = f'{movementInput.lower()}_to'
        print(f'\n\nYou have selected {movementInput.capitalize()}')

        if (movementInput.lower() not in ['n', 's', 'e', 'w', 'c', 'q']):
            print(f'{movementInput.capitalize()} is not a valid selection.')
            movementInput = input(movementMessage)
        elif (movementInput.lower() == 'q'):
            exit()
        elif (movementInput.lower() == 'c'):
            print(breaktext)
            print(f'Current room: {player.room}')
            print(breaktext)
        elif (getattr(player.room, command) != None):
            player.room = getattr(player.room, command)

            print(breaktext)
            print(f'{player}\n')
            player.room.print_items();
            print(breaktext)

        else:
            mystring = ""
            for attr, value in player.room.__dict__.items():
                if (isinstance(value, Room)):
                    letter = (str(attr[0]).capitalize())
                    mystring = f"{mystring} {letter}"
            print(f"Please try again! o(╥﹏╥)o\nYou may only move in the following direction(s):{mystring}")
            print(breaktext)
        menuInput = input(menuMessage)


    while (menuInput.lower() == 'i'):
        itemMessage = "Take or drop an item?\nType 'back to menu' to return to menu\n >> "
        print(breaktext)
        print("Inventory: ")
        player.print_items()
        print(breaktext)
        print("Items from on the floor: ")
        player.room.print_items()
        print(breaktext)
        itemInput = input(itemMessage)
        command = itemInput.split()[0].lower()

        # Check to make sure item name is passed in to keep from breaking game
        while (itemInput.split().__len__() < 2):
            itemInput = input('Please include an item name.\n' + itemMessage)

        item = itemInput.split()[1].lower()

        
        if (command == 'take'):
            for i in player.room.avaliableItems:
                if (i.name.lower() == item):
                    
                    player.pickup(i)
                    player.room.remove_item(i)

            
        elif (command == 'drop'):
            for i in player.inventory:
                if(i.name.lower() == item):

                    player.drop_item(i)
                    player.room.add_item(i)

        elif (command == 'back'):
            menuInput = input(menuMessage)

        elif (command != 'take' or command != 'drop' or command != 'back'):
            itemInput = input('Not a valid command.\n' + itemMessage)

    if (menuInput != 'm' or menuInput != 'i'):
        print(breaktext)
        menuInput = input(menuMessage)
        print(breaktext)
