from turtle import Turtle, Screen

turtle_ui = Turtle()
turtle_ui.shape("turtle")
turtle_ui.color("red")


def draw_square():
    for _ in range(4):
        turtle_ui.forward(100)
        turtle_ui.left(90)
        
def draw_sqaure_dash():
     for _ in range(4):
        for _ in range(5):
            turtle_ui.forward(10)
            turtle_ui.penup()
            turtle_ui.forward(10)
            turtle_ui.pendown()
      
        turtle_ui.left(90)

draw_sqaure_dash()









screen =  Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())