import turtle as t
import random as rd
import time as tm

# Set up screen
t.bgcolor('yellow')

# Set up caterpillar
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('green')
caterpillar.speed(0)
caterpillar.penup()

# Set up leaf
leaf = t.Turtle()
leaf.shape('circle')
leaf.color('red')
leaf.penup()
leaf.speed(0)
leaf.setposition(rd.randint(-200, 200), rd.randint(-200, 200))

# Set up text turtle
text_turtle = t.Turtle()
text_turtle.write('Press Space to Start', align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

# Set up score turtle
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)
score_turtle.penup()
score_turtle.setposition(0, 200)
score = 0

# Functions to move the caterpillar
def move_up():
    if caterpillar.heading() != 270:  # Prevent moving in the opposite direction
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() != 90:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() != 0:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() != 180:
        caterpillar.setheading(0)

# Function to start the game
def start_game():
    global score
    score = 0
    text_turtle.clear()
    caterpillar.setposition(0, 0)
    caterpillar.showturtle()
    leaf.setposition(rd.randint(-200, 200), rd.randint(-200, 200))
    score_turtle.clear()
    score_turtle.write(f'Score: {score}', align='center', font=('Arial', 18, 'bold'))
    
    while True:
        caterpillar.forward(20)
        
        if caterpillar.distance(leaf) < 20:
            leaf.setposition(rd.randint(-200, 200), rd.randint(-200, 200))
            score += 10
            score_turtle.clear()
            score_turtle.write(f'Score: {score}', align='center', font=('Arial', 18, 'bold'))
        
        # Game over conditions
        if abs(caterpillar.xcor()) > 200 or abs(caterpillar.ycor()) > 200:
            caterpillar.hideturtle()
            text_turtle.write(f'Game Over! Your score: {score}', align='center', font=('Arial', 18, 'bold'))
            break
        
        tm.sleep(0.1)

# Keyboard bindings
t.listen()
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')

t.mainloop()
