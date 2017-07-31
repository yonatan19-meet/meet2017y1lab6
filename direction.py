UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"

UP = 0
direction = UP

def up():
    global direction
    direction = UP
    print('You pressed Up')

def down():
    global direction
    direction = DOWN
    print('You pressed Down')

def left():
    global direction
    direction = LEFT
    print('You pressed Left')

def right():
    global direction
    direction = RIGHT
    print('You pressed Right')

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
