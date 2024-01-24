from turtle import Turtle,Screen
import random
is_race_on=False
colors=["violet","blue","green","yellow","orange","red"]
screen=Screen()
screen.setup(height=400,width=500)
user_bet=screen.textinput(title="Place your bet",prompt="Who do you think is going to win the race?Enter a color:")
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
for i in range(6):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=y_positions[i])
    all_turtles.append(tim)
if user_bet:
    is_race_on=True
while is_race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            is_race_on = False
            if user_bet == i.pencolor():
                print(f"You won! Turtle {i.pencolor()} is the winner.")
            else:
                print(f"You lost! Turtle {i.pencolor()} is the winner.")
        i.forward(random.randint(0,10))
screen.exitonclick()