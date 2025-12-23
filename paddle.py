from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super(). __init__()
        self.shape("square")
        
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.color('white')
        self.goto(position)
    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)


    # def move_up(self):
    #     new_y = self.ycor() + 20
    #     self.goto(self.xcor(), new_y)

    # def move_down(self):
    #     new_y = self.ycor() - 20
    #     self.goto(self.xcor(), new_y)











