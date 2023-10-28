import turtle

# Create the screen
screen_1 = turtle.Screen()
screen_1.title("Ping-Pong Game")
screen_1.bgcolor("Yellow")
screen_1.setup(width=1050, height=650)

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("Red")
left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-400, 0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("Blue")
right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(400, 0)

# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(45)
hit_ball.shape("circle")
hit_ball.color("Black")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Initialize the score
player_one = 0
player_two = 0
max_score = 5  # Set the maximum score to trigger "game over" when a player reaches 10

# Display the score
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("blue")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player One: 0    Player Two: 0", align="center", font=("Courier", 24, "normal"))

# Implementing the functions for moving paddles vertically
def paddle_L_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def paddle_L_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def paddle_R_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def paddle_R_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Binding keys for moving the paddles up and down
screen_1.listen()
screen_1.onkeypress(paddle_L_up, "r")
screen_1.onkeypress(paddle_L_down, "c")
screen_1.onkeypress(paddle_R_up, "Up")
screen_1.onkeypress(paddle_R_down, "Down")

# Initialize game over flag
game_over = False

# Main game loop
while True:
    screen_1.update()

    if game_over:
        # Display "Game Over" message and replay/quit options at the top of the screen
        score_display.clear()
        if player_one >= max_score:
            score_display.goto(0, 100)
            score_display.write("Player One Wins!", align="center", font=("Courier", 24, "normal"))
        else:
            score_display.goto(0, 100)
            score_display.write("Player Two Wins!", align="center", font=("Courier", 24, "normal"))
        score_display.goto(0, 0)
        score_display.write("Game Over", align="center", font=("Courier", 36, "normal"))
        score_display.goto(0, -50)
        score_display.write("Press 's' to replay or 'q' to quit", align="center", font=("Courier", 18, "normal"))

        # Check for replay or quit
        screen_1.listen()
        screen_1.onkeypress(replay_game, "s")
        screen_1.onkeypress(quit_game, "q")
    else:
        hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
        hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

        # Check all the borders
        if hit_ball.ycor() > 280:
            hit_ball.sety(280)
            hit_ball.dy *= -1

        if hit_ball.ycor() < -280:
            hit_ball.sety(-280)
            hit_ball.dy *= -1

        if hit_ball.xcor() > 500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            player_one += 1
            score_display.clear()
            score_display.write("Player One: {}    Player Two: {}".format(player_one, player_two), align="center",
                                font=("Courier", 24, "normal"))
            if player_one >= max_score:
                game_over = True

        if hit_ball.xcor() < -500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            player_two += 1
            score_display.clear()
            score_display.write("Player One: {}    Player Two: {}".format(player_one, player_two), align="center",
                                font=("Courier", 24, "normal"))
            if player_two >= max_score:
                game_over = True

        # Collision of ball and paddles
        if (hit_ball.xcor() > 360 and 340 < hit_ball.xcor()) and (right_paddle.ycor() + 50 > hit_ball.ycor() > right_paddle.ycor() - 50):
            hit_ball.setx(340)
            hit_ball.dx *= -1

        if (hit_ball.xcor() < -360 and -340 > hit_ball.xcor()) and (left_paddle.ycor() + 50 > hit_ball.ycor() > left_paddle.ycor() - 50):
            hit_ball.setx(-340)
            hit_ball.dx *= -1

    # Function to replay the game
    def replay_game():
        global player_one, player_two, game_over
        player_one = 0
        player_two = 0
        game_over = False
        score_display.clear()
        score_display.write("Player One: 0    Player Two: 0", align="center", font=("Courier", 24, "normal"))
        hit_ball.goto(0, 0)

    # Function to quit the game
    def quit_game():
        turtle.bye()
        
