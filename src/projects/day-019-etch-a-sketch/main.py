from turtle import Turtle, Screen

# Screen
screen = Screen()
screen.setup(600, 450)
screen.bgcolor("lightgrey")

# Border
border = Turtle()
border.hideturtle()
border.penup()
border.speed(0)
border.goto(-275, 200)
border.pendown()

border.color("red")
border.pensize(10)

for _ in range(2):
    border.forward(550)
    border.right(90)
    border.forward(400)
    border.right(90)


width, height = 550, 400

# Create the turtle for drawing
t = Turtle()
t.speed(0)
t.pensize(2)
instructions_visible = True


def move_with_boundary_check(x, y):
    if -width//2 + 5 < x < width//2 - 5 and -height//2 + 5 < y < height//2 - 5:
        t.goto(x, y)


def move_left():
    move_with_boundary_check(t.xcor() - 5, t.ycor())


def move_right():
    move_with_boundary_check(t.xcor() + 5, t.ycor())


def move_up():
    move_with_boundary_check(t.xcor(), t.ycor() + 5)


def move_down():
    move_with_boundary_check(t.xcor(), t.ycor() - 5)


def save_drawing():
    ts = t.getscreen()
    ts.getcanvas().postscript(file="drawing.eps")


def reset():
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()


def toggle_eraser():
    if t.pencolor() == "lightgrey":
        t.pencolor("black")
    else:
        t.pencolor("lightgrey")


instructions = (
        "Keybinds:\n"
        "W - Move Up\n"
        "S - Move Down\n"
        "A - Move Left\n"
        "D - Move Right\n"
        "E - Toggle Eraser\n"
        "G - Save Drawing\n"
        "R - Reset\n"
        "H - Display/Hide Instructions\n"
    )


def display_instructions():
    global info_turtle
    info_turtle = Turtle()
    info_turtle.hideturtle()
    info_turtle.penup()
    info_turtle.goto(0, 0)
    info_turtle.write(instructions, align="center", font=("Arial", 12, "normal"))


# Display the instructions on the screen
display_instructions()


def hide_instructions():
    info_turtle.clear()


# Function to toggle instructions visibility
def toggle_instructions():
    global instructions_visible
    if instructions_visible:
        hide_instructions()
        instructions_visible = False
    else:
        display_instructions()
        instructions_visible = True


# Keybinds
screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(save_drawing, "g")
screen.onkey(reset, "r")
screen.onkey(toggle_eraser, "e")
screen.onkey(toggle_instructions, "h")

screen.mainloop()