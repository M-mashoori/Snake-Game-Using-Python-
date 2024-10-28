import turtle
import time
import random

delay = 0.1
score = 0
highestscore = 0

bodies = []

# Main Screen
main_screen = turtle.Screen()
main_screen.title("Snake Game")
main_screen.bgcolor('green')
main_screen.setup(width=600, height=600)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.fillcolor('blue')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('yellow')
food.fillcolor('red')
food.penup()
food.goto(0, 200)

# Score Board
sb = turtle.Turtle()
sb.shape('square')
sb.fillcolor('black')
sb.penup()
sb.ht()
sb.goto(-280, 250)
sb.write('Score: 0  | HighestScore: 0', font=('arial', 15, 'bold'))

# Function Declaration
def moveup():
    if head.direction != 'down':
        head.direction = 'up'

def movedown():
    if head.direction != 'up':
        head.direction = 'down'

def moveleft():
    if head.direction != 'right':
        head.direction = 'left'

def moveright():
    if head.direction != 'left':
        head.direction = 'right'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

# Event Handling
main_screen.listen()
main_screen.onkey(moveup, 'Up')
main_screen.onkey(movedown, 'Down')
main_screen.onkey(moveleft, 'Left')
main_screen.onkey(moveright, 'Right')

# Main loop
try:
    while True:
        main_screen.update()

        # Check collision with walls
        if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # Hide bodies
            for body in bodies:
                body.goto(1000, 1000)  # Move out of sight
            bodies.clear()

            # Reset score and delay
            score = 0
            delay = 0.1

            # Update score board
            sb.clear()
            sb.write('Score: {} | HighestScore: {}'.format(score, highestscore), font=('arial', 15, 'bold'))

        # Check collision with food
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Increase the length of snake
            body = turtle.Turtle()
            body.speed(0)
            body.shape('square')
            body.color('red')
            body.fillcolor('darkred')
            body.penup()
            bodies.append(body)

            # Increase the score
            score += 10

            # Decrease delay
            delay -= 0.001

            # Update the highest score
            if score > highestscore:
                highestscore = score
            sb.clear()
            sb.write('Score: {} | HighestScore: {}'.format(score, highestscore), font=('arial', 15, 'bold'))

        # Move the snake body
        for i in range(len(bodies) - 1, 0, -1):
            x = bodies[i - 1].xcor()
            y = bodies[i - 1].ycor()
            bodies[i].goto(x, y)

        if len(bodies) > 0:
            x = head.xcor()
            y = head.ycor()
            bodies[0].goto(x, y)

        move()

        # Check collision with snake body
        for body in bodies:
            if body.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = 'stop'

                # Hide bodies
                for body in bodies:
                    body.goto(1000, 1000)  # Move out of sight
                bodies.clear()

                score = 0
                delay = 0.1

                # Update score board
                sb.clear()
                sb.write('Score: {} | HighestScore: {}'.format(score, highestscore), font=('arial', 15, 'bold'))

        time.sleep(delay)

except turtle.Terminator:
    print("The game window was closed.")

main_screen.mainloop()
