from turtle import Turtle, Screen

ui = Turtle()
screen = Screen()


def move_forward():
    ui.forward(10)
    
def move_backward():
    ui.backward(10)

def move_counter_clockwise():
    ui.left(10)

def move_clockwise():
    ui.right(10)
    
def clear():
    ui.clear()
    ui.penup()
    ui.home()
    ui.pendown()


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward, "s")
screen.onkey(move_counter_clockwise,"a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear, "space")
screen.exitonclick() 