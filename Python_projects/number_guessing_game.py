import random

attempt = 10
computer_num = 0
difficulty_sel =""

def difficulty(difficulty_sel):
    """Assigns the attempts to user"""
    global attempt
    if difficulty_sel == "h":  # Hard mode
        attempt = 5
    elif difficulty_sel == 'e':  # Easy mode
        attempt = 10 

def computer_pick():
    global computer_num
    computer_num = random.randint(1, 100)

print("Welcome to the number guessing game. I am thinking of a number between 1 and 100")

def game():
    global difficulty_sel
    global attempt
    difficulty_sel = str(input("Choose a difficulty. Type 'e' for easy, 'h' for hard:"))
    difficulty(difficulty_sel)
    computer_pick()
    while attempt > 0:
        print(f'You have {attempt} remaining to guess the number.')
        guess = int(input("Make a guess:"))
        if guess > computer_num:
            print("Too high. Guess again")
        else:
            print("Too low. Guess again")
        attempt= attempt - 1
        if attempt == 0: 
            print(f'Ohh no you lose, The number was {computer_num}.')

game()

while input("Do you want to play again? Type 'y' for yes or 'n' for no.") == 'y':
    game()