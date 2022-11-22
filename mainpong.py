from turtle import Screen,Turtle
from paddel import Paddel
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
r_paddel=Paddel((350,0))
l_paddel=Paddel((-350,0))

ball=Ball()
score = Scoreboard()




screen.listen( )
screen.onkey(r_paddel.go_up,"Up")
screen.onkey(r_paddel.go_down,"Down")
screen.onkey(l_paddel.go_up,"w")
screen.onkey(l_paddel.go_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # /Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    # Detect collision with paddel
    if ball.distance(r_paddel)<50 and ball.xcor()>320 or ball.distance(l_paddel)<50 and ball.xcor()<-320:
        ball.bounce_x()
        
           
    if ball.xcor()>380:
        ball.reset_position() 
        score.l_update()
    if ball.xcor()<-380:
        ball.reset_position() 
        score.r_update()   
        
screen.exitonclick() 



 