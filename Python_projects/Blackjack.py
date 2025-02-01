import random
from art import *

def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes in a users_score and computers score """
    if sum(cards)==21 in cards and len(cards) ==2: 
        return 0
    
    if 11 in cards and sum(cards) > 21: 
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent had Blackjack !!!" 
    elif u_score == 0:
        return "WIN!! with Blackjack !!!"
    elif u_score > 21: 
        return "You went over. You lose"
    elif c_score > 21: 
        return "Opponent went over. You WIN!!!"
    elif u_score > c_score:
        return "YOU WIN !!!"
    else:
        return "YOU LOSE!!"

def play_game():    
    tprint("BLACKJACK")

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_to_deal = input("Type 'y' to get another card or type 'n' to pass:")
            if user_to_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} and final score is {user_score}")
    print(f"Computer final hand: {computer_cards} and final score is {computer_score}")
    print(compare(user_score, computer_score))

while input(f"Do you want to play a game of Blackjack? Type 'y' or 'n'") =='y':
    print("\n" *20)
    play_game()