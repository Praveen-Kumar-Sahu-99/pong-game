from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# class Display(Screen):
#     def __init__(sreen):
#         super().__init__()
sreen = Screen()
sreen.setup(width=800,height =600)
sreen.bgcolor('black')
sreen.title("My pong game")
sreen.tracer(0)
l_paddle =Paddle((-350,0))
r_paddle = Paddle((350,0))
ball =Ball()
score= Score()
sreen.listen()
sreen.onkeypress(r_paddle.move_up,"i")
sreen.onkeypress(r_paddle.move_down,"k")

sreen.onkeypress(l_paddle.move_up,"w")
sreen.onkeypress(l_paddle.move_down,"s")

game_is_on = True
while game_is_on:
    sreen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #detet collision wth wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.boune_y()
    #detect colliosn with Paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor() <-320 :
        ball.boune_x()
    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    #Detet L Paddle misses
    if ball.xcor() <-380:
        ball.reset_position()
        score.r_point()

sreen.exitonclick()