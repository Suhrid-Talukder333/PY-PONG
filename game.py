import turtle
import os
wn = turtle.Screen()
wn.title("Pong (suhrid)")
wn.bgcolor("black")
wn.setup(width= 920,height= 690)
wn.tracer(0)

#paddle A
paddle_a=turtle.Turtle()
paddle_a.penup()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.goto(-400,0)
paddle_a.shapesize(stretch_len=1,stretch_wid=5)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.penup()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.goto(400,0)
paddle_b.shapesize(stretch_len=1,stretch_wid=5)

#BALL
ball=turtle.Turtle()
ball.penup()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.goto(0,0)
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.dx= 1
ball.dy= -1

#Ceiling up
ceiling_up=turtle.Turtle()
ceiling_up.shape("square")
ceiling_up.goto(0,395)
ceiling_up.shapesize(stretch_len= 100, stretch_wid= 10)
ceiling_up.color("white")

#ceiling down
ceiling_down=turtle.Turtle()
ceiling_down.shape("square")
ceiling_down.goto(0,-395)
ceiling_down.shapesize(stretch_len= 100, stretch_wid= 10)
ceiling_down.color("white")

#Score Board
score_board=turtle.Turtle()
score_board.color("green")
score_board.speed(0)
score_board.penup()
score_board.goto(0,0)
score_board.write("Player A : 0|||||||||Player B : 0", align="center", font=("Courier", 20, "normal"))

#score
score_a=0
score_b=0

#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard bindings
wn.listen()
wn.onkey(paddle_a_up,"w")
wn.onkey(paddle_a_down,"s")
wn.onkey(paddle_b_up,"Up")
wn.onkey(paddle_b_down,"Down")


while True:
    wn.update()

    #ball_movemnt
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav")
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        os.system("aplay bounce.wav")
        score_board.clear()
        score_a += 1
        score_board.write("Player A : {}|||||||||Player B : {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        os.system("aplay bounce.wav")
        score_board.clear()
        score_b += 1
        score_board.write("Player A : {}|||||||||Player B : {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav")
#ball and paddle collision
    if (ball.xcor() > 380 and ball.xcor() < 390) and (ball.ycor() < paddle_b.ycor() +80 and ball.ycor() > paddle_b.ycor() -80):
        ball.setx(380)
        ball.dx *= -1
    if (ball.xcor() < -380 and ball.xcor() > -390) and (ball.ycor() < paddle_a.ycor() +80 and ball.ycor() > paddle_a.ycor() -80):
        ball.setx(-380)
        ball.dx *= -1
