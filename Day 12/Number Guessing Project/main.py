from random import randint
from art import logo
EASY_NUMBER_TURN = 10
HARD_NUMBER_TURN = 5
def check_answer(user_answer,actual_answer,turn):
    if user_answer > actual_answer:
        print("Too High")
        return turn -1
    elif user_answer < actual_answer:
        print("Too low")
        return turn -1
    else:
        print(f"you got it!{actual_answer}")

def set_difficulty():
    print(logo)
    level = input("choose a difficulty. Type 'easy' or 'Hard':")
    if level == 'easy':
        return EASY_NUMBER_TURN
    else:
        return HARD_NUMBER_TURN
def game():
    print("Welcome to the number guessing game")
    print("I am Thinking of the number between 1 to 100")
    answer = randint(1,100)

    turn = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"you have {turn} attempt remain!")
        guess = int(input("Make a guess:"))
        turn = check_answer(guess,answer,turn)
        if turn == 0:
            print("You are out of the range")
            return
game()


