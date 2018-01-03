# New main file
from player import Player, test_win, inquire
from display import screen, start_screen, screen_next

# START: Basic Startup
start_screen()

player1 = Player('player1')
player2 = Player('player2')
#player3 = Player('player3')

player_list = [player1, player2] #, player3]
player_dict = {'player1': player1, 'player2': player2} #,'player3': player3}

for player in player_list:
    player.start_dict(player_dict)
    response = player.pickup_cards(player)
    player.sort_cards()
# END: Basic Startup

# If this isn't the messiest game ever made, i don't know what is
while True:
    for player in player_list:

        current_cards = len(player.cards)
        inquire_run = 0

        while True:
            player.look_for_sets()
            test_win(player_dict)

            action = input('> ')

            if action == 'inquire':

                if len(player.cards) == current_cards and inquire_run > 0:
                    response = ['You have already asked and failed.',
                                'Pick up a card instead.']
                    screen(response, player)

                elif len(player.cards) == current_cards and inquire_run == 0:
                    response = inquire(player)
                    screen(response, player)
                    inquire_run += 1

                    if len(player.cards) > current_cards:
                        input()
                        screen_next()
                        input()
                        break

                else:
                    response =["You can't do that."]
                    screen(response, player)


            elif action == 'pick':

                if len(player.cards) == current_cards and inquire_run == 0:
                    response = ["You first have to ask for a card..."]
                    screen(response, player)

                elif len(player.cards) == current_cards and inquire_run > 0:
                    response = player.pickup_cards(player)
                    screen(response, player)
                    input()
                    screen_next()
                    break

                elif len(player.cards) > current_cards and inquire_run == 1:
                    response = ["You can't pick up anything."]
                    screen(response, player)

                else:
                    response = ["pick NONE"]
                    screen(response, player)


            elif action == '?':
                response = ['Available options:', 'pick, inquire']

            else:
                response = ['']
                screen(response, player)
