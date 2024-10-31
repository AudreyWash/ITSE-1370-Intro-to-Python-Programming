from itertools import product
from random import choice, seed
from os import linesep

suits = ['clubs', 'diamonds', 'hearts', 'spades']
numbers = list(range(2, 15))  
a = 551
seed(a)

def create_standard_deck():
    deck = []
    for suit in suits:
        for number in numbers:
            deck.append((suit, number))
    return deck


def draw_card(deck):
    card = choice(deck)
    deck.remove(card)
    return card


def get_count(player):
    total = 0
    ace_count = 0

    for card in player:
        value = card[1]
        if value >= 11 and value <= 13:  
            total += 10
        elif value == 14:  
            total += 11
            ace_count += 1
        else:
            total += value

    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1

    return total


def check_cards(player):
    total = get_count(player)
    if total == 21:
        return 'WIN'
    elif total > 21:
        return 'BUST'
    else:
        return 'OK'


def display_dealer(opponent, start=False):
    print('Dealer:')
    if start:
        print([opponent[0], ('?', '?')])
    else:
        print(opponent)


def display_player(player):
    print('Player:')
    print(player)


def create_blackjack_game(user_input):
    
    player = []
    dealer = []
    deck = create_standard_deck()

    
    for _ in range(2):
        player.append(draw_card(deck))
        dealer.append(draw_card(deck))

    
    display_player(player)
    display_dealer(dealer, start=True)

    
    player_action = input('Press h to hit, s to stand, q to quit: ').lower().strip(linesep)
    while player_action not in ('s', 'h', 'q'):
        player_action = input('Press h to hit, s to stand, q to quit: ').lower().strip(linesep)

    if player_action == 'q':
        return 0

    while player_action != 'q':
        if player_action == 'h':
            
            player.append(draw_card(deck))
            display_player(player)

            
            result = check_cards(player)
            if result == 'WIN':
                print("You win!")
                return 1
            elif result == 'BUST':
                print("You busted! Dealer wins.")
                return -1
            else:
                print("You still have room to hit.")

        else:  
            
            while get_count(dealer) < 17:
                dealer.append(draw_card(deck))
            display_dealer(dealer, start=False)

            dealer_result = check_cards(dealer)
            if dealer_result == 'WIN':
                print("Dealer wins with 21!")
                return -1
            elif dealer_result == 'BUST':
                print("Dealer busted! You win!")
                return 1

            
            player_total = get_count(player)
            dealer_total = get_count(dealer)
            if player_total > dealer_total:
                print("You win!")
                return 1
            else:
                print("Dealer wins!")
                return -1

        player_action = input('Press h to hit, s to stand, q to quit: ').lower().strip(linesep)
        while player_action not in ('s', 'h', 'q'):
            player_action = input('Press h to hit, s to stand, q to quit: ').lower().strip(linesep)

    return 0