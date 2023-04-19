from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet","Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_postions = [-70, -40, -10, 20, 50, 80]
turtles = []
for index in range(0, len(colors)):
    print(index)
    turtle = Turtle("turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(-230, y_postions[index])
    turtles.append(turtle)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            if(turtle.color() == user_bet.lower()):
                print(f"You have won! The {user_bet} turtle is the winner")
            else:
                print("Loser!")
            is_race_on =False
                

        turtle.forward(random.randint(0,10))

screen.exitonclick()