"""War Card Game"""
from player import Player
from deck import Deck

# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
    player_one.add_card(new_deck.deal_card())
    player_two.add_card(new_deck.deal_card())

GAME_ON = True
ROUND_NUM = 0

while GAME_ON:

    ROUND_NUM += 1
    print(f"Round {ROUND_NUM}")

    if len(player_one.all_cards) == 0:
        print("\nPlayer One, out of cards!\nPLAYER TWO WINS!")
        GAME_ON = False
        break
    if len(player_two.all_cards) == 0:
        print("\nPlayer Two, out of cards!\nPLAYER ONE WINS!")
        GAME_ON = False
        break

    # Start a new round
    player_one_cards = [player_one.remove_card()]
    player_two_cards = [player_two.remove_card()]

    AT_WAR = True

    while AT_WAR:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)

            AT_WAR = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)

            AT_WAR = False

        else:
            print("WAR!")

            if len(player_one.all_cards) < 5:
                print("\nPlayer One unable to declare war!\nPLAYER TWO WINS!")
                AT_WAR = False
                GAME_ON = False

            elif len(player_two.all_cards) < 5:
                print("\nPlayer Two unable to declare war!\nPLAYER ONE WINS!")
                AT_WAR = False
                GAME_ON = False

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
