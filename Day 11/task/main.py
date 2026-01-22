import random
from art import logo

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose opponent have jackpot"
    elif u_score == 0:
        return "Win with a jackpot"
    elif u_score >21:
        return "You Lose"
    elif c_score > 21:
        return "opponent went over . You Win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You Lose"
def play_game():
    print(logo)
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1

    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your Card {user_card},current score:{user_score}")
        print(f"computer's first card {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
             user_want_another_card = input("Type 'y' to get another cards,type 'n' to pass:")
             if user_want_another_card == "y":
                 user_card.append(deal_card())
             else:
                 is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"your final hand:{user_card},final score:{user_score}")
    print(f"computer score:{computer_card},final score:{computer_score}")
    print(compare(user_score,computer_score))

while input("Type 'y' if you want to restart the game or type 'n' for stay here not restart the game:") == "y":
      print("\n")
      play_game()