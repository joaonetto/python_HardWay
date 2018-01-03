# contains the player class
# each function in Player needs to return a list with the responses in it.
import random
from display import screen

def fill_cards(): # fills/shuffles cards list
    types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards = []
    for single_type in types:
        for line in range(4):
            cards.append(single_type)

    random.shuffle(cards)
    return cards

class Player(object):
    # I'm going to try to finish the game without adding any extra methods to this.

    cards = fill_cards()

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.player_dict = {}
        self.card_sets = []

    def pickup_cards(self, player):
        if Player.cards == []:
            response = ['The main deck is empty.',
                        'It is now the next players turn']
            return response

        elif len(self.cards) == 0 and len(Player.cards) > 5:
            for i in range(5):
                self.cards.append(Player.cards.pop())
            response = ['You picked up 5 cards.']
            return response

        elif len(self.cards) == 0 and len(Player.cards) <= 5:
            for i in range(len(cards)):
                self.cards.append(Player.cards.pop())
            response = ["You picked up {} cards".format(len(Player.cards))]
            return response

        elif len(self.cards) >= 1 and len(Player.cards) >= 1:
            card = Player.cards.pop()
            self.cards.append(card)
            response = [f"You picked up 1 '{card}' card."]
            return response

        else:
            response_list = ['pickup_cards else']
            return response

    def show_cards(self):
        self.sort_cards()

        if self.cards == []:
            print('Cards: None')
        else:
            print(f'Cards: {self.cards}')

    def show_sets(self):
        if self.card_sets == []:
            print("Sets: None")

        else:
            print(f'Sets: {self.card_sets}\n')

    def sort_cards(self):

        forward_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                        'J': 11, 'Q': 12, 'K': 13}
        backward_dict = {y:x for x, y in forward_dict.items()}

        output_list = []
        temp_list = []

        # forward
        for i in self.cards:
            temp_list.append(forward_dict[i])

        # sort
        temp_list.sort()

        # backward
        for i in temp_list:
            output_list.append(backward_dict[i])

        del self.cards[:]
        self.cards = output_list[:]

    def start_dict(self, player_dict):
        self.player_dict = dict(player_dict)
        del self.player_dict[self.name]

    def look_for_sets(self):
        types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in types:
            if self.cards.count(i) >= 4:
                for x in range(4):
                    self.cards.remove(i)

                self.card_sets.append(i)


# Checks to see it someone in the game won
def test_win(player_dict):

    empty = 0

    for k, v in player_dict.items():
        if len(v.cards) == 0:
            empty += 1

    if len(Player.cards) == 0 and empty == len(player_dict):
        print("End game!")

        temp_dict = {}

        for k, v in player_dict.items():
            v.look_for_sets()
            temp_dict[v.name] = len(v.card_sets)

        winner = max(temp_dict, key=temp_dict.get)
        print(f'{winner} won!')
        exit(0)

def check_inquire_input(player, choice_player, choice_card):
    types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    choice_player = choice_player.strip().lower()
    choice_card = choice_card.strip().upper()

    if choice_player not in player.player_dict:
        print("Invalid Player.")
        print('Re-enter your player choice.')
        choice_player = input('Enter the player name -> ')
        check_inquire_input(player, choice_player, choice_card)

    elif choice_card not in types:
        print("Invalid Card Type.")
        print('Re-enter your card choice.')
        choice_card = input('Enter the card type -> ')
        check_inquire_input(player, choice_player, choice_card)

    return choice_player, choice_card

def inquire(player):
    current_cards = len(player.cards)
    response = ['Inquire']
    while True:
        screen(response, player)

        choice_player = input('Enter the player name -> ')
        choice_card = input('Enter the card type -> ')

        choice_player, choice_card = check_inquire_input(player, choice_player, choice_card)

        taken = 0
        if choice_card in player.player_dict[choice_player].cards:
            for i in player.player_dict[choice_player].cards:
                if choice_card == i:
                    player.cards.append(choice_card)
                    taken += 1

            for _ in range(taken):
                player.player_dict[choice_player].cards.remove(choice_card)

            response = [f"You took {taken} '{choice_card}' card from {choice_player}.",
                         "You can ask another time."]

        elif choice_card not in player.player_dict[choice_player].cards and current_cards == len(player.cards):
            response = [f"{choice_player} didn't have any '{choice_card}' cards.",
                         "Pick up a card instead."]
            return response

        elif choice_card not in player.player_dict[choice_player].cards and current_cards < len(player.cards):
            response = [f"{choice_player} didn't have any '{choice_card}' cards."]
            return response

        else:
            response = ['LOCATION inquire(): INPUT INVALID']
            screen(response, player)
