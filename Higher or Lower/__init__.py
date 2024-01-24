from art import logo
from art import vs
print(logo)
from game_data import data
import random
A=random.choice(data)
B=random.choice(data)
while A==B:
    B=random.choice(data)
print(f"Compare A:{A['name']}, a {A['description']}, from {A['country']}.")
print(vs)
print(f"Against B:{B['name']}, a {B['description']}, from {B['country']}.")
choice=input("Which do you think has more followers? Type A or B:")
def ans(A,B):
    if A['follower_count']>B['follower_count']:
        return A
    else:
        return B
score=0
if ans(A,B)==A:
    answer='A'
else:
    answer='B'
print(answer)
while(choice==answer):
    score+=1
    print(f"Correct answer!Current Score:{score}")
    A=ans(A,B)
    B=random.choice(data)
    while(A==B):
        B=random.choice(data)
    print(f"Compare A:{A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B:{B['name']}, a {B['description']}, from {B['country']}.")
    choice = input("Which do you think has more followers? Type A or B:")
    if ans(A,B)==A:
        answer='A'
    else:
        answer='B'
print(f"Wrong answer! Your score:{score}")