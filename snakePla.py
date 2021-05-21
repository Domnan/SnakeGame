import turtle
import time
import random

# creating the screen
screen = turtle.Screen()
screen.title("Hungry Viper")
screen.setup(width=500, height=500)
screen.bgcolor("teal")
screen.tracer(0)


# creating the snake head
head = turtle.Turtle()
head.penup()
head.shape("triangle")
head.color("white")
head.goto(0,0)
head.direction = "stop"
head.speed(0)

# food
food = turtle.Turtle()
food.penup()
food.direction = "stop"
food.shape("square")
food.color("black")
x = random.randint(-200,200)
y = random.randint(-200,200)
food.goto(x,y)

# creating the body
snake = []


# fuctions
def sama():
    head.direction = "up"
def kasa():
    head.direction = "down"
def dama():
    head.direction = "right"
def hagu():
    head.direction = "left"

def tafi():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)
# key binding
screen.listen()
screen.onkey(sama, "Up")
screen.onkey(kasa, "Down")
screen.onkey(dama, "Right")
screen.onkey(hagu, "Left")

# main game loop
while True:
    screen.update()
    if head.distance(food) < 20:
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.penup()
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.speed(0)

        snake.append(new_segment)
        # moving the end segments first in reverse order
    for index in range(len(snake)-1,0,-1):
        x = snake[index-1].xcor()
        y = snake[index-1].ycor()
        snake[index].goto(x,y)
        # for moving segment 0 to where the head is
    if len(snake) >0:
        x = head.xcor()
        y = head.ycor()
        snake[0].goto(x,y)
    tafi()
    time.sleep(0.1)



    

screen.mainloop()
