import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
user_cards=[]
computer_cards=[]
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
is_game_over=False
while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards:{user_cards},your score:{user_score}")
    print(f"Computer's first card:{computer_cards[0]}")
    if user_score==21 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("Enter 'y' to deal another card/Enter 'n' to pass:")
        if user_should_deal=='y':
            user_cards.append(deal_card())
        elif user_should_deal=='n':
            is_game_over=True
while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)