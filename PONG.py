import turtle

wn=turtle.Screen()
wn.setup(width = 800, height = 600)
wn.bgcolor("black")
wn.title("Shurid pong")
wn.tracer(0)

#paddle_A
paddle_a=turtle.Turtle()
paddle_a.penup()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)

#paddle_B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.penup()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball=turtle.Turtle()
ball.penup()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.goto(0,0)
ball.dx = .5
ball.dy = -.5

#functions
def padlle_a_up():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def padlle_a_down():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def padlle_b_up():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def padlle_b_down():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(padlle_a_up, "w")
wn.onkeypress(padlle_a_down, "s")
wn.onkeypress(padlle_b_up, "Up")
wn.onkeypress(padlle_b_down, "Down")


#main loop
while True:
    wn.update()

    #ball_movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #gameplay
    if ball.xcor() > 400 :
        ball.goto(0,0)
        
    if ball.xcor() < -400 :
        ball.goto(0,0)
        
    #collisions
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *=-1
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50 ):
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50 ):
        ball.setx(-340)
        ball.dx *= -1