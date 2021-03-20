import turtle
import random

#set up our screen
screen = turtle.Screen()
screen.tracer(0)




def branch(x,y,angle,changeAngle,length,thiccness,killswitch):
  if(killswitch>0):
    pen = turtle.Turtle()
    pen.speed(0)
    
    #move into position and point the right way
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.setheading(angle)
    pen.pensize(thiccness)
    
    #draw the line
    pen.forward(length)
    pen.hideturtle()
    if(killswitch>2):
      screen.update()
    
    #calculate angle of each branch
    newAngle1 = angle + changeAngle + random.randint(0,5)
    newAngle2 = angle + changeAngle/2 + random.randint(0,5)
    newAngle3 = angle  + random.randint(-5,5)
    newAngle4 = angle - changeAngle/2 - random.randint(0,5)
    newAngle5 = angle - changeAngle - random.randint(0,5)
    
    #calculate the length of each branch using the golden ratio
    newLength1 = length * (1/1.6180) + random.randint(-5,5)
    newLength2 = length * (1/1.6180) + random.randint(-5,5)
    newLength3 = length * (1/1.6180) + random.randint(-5,5)
    newLength4 = length * (1/1.6180) + random.randint(-5,5)
    newLength5 = length * (1/1.6180) + random.randint(-5,5)
    
    #calculate the thiccness of each branch
    newThiccness1 = thiccness / 2
    newThiccness2 = thiccness / 2
    newThiccness3 = thiccness / 2
    newThiccness4 = thiccness / 2
    newThiccness5 = thiccness / 2
    
    #call the branch function 5 times
    branch(pen.xcor(),pen.ycor(),newAngle1,changeAngle/2,newLength1,newThiccness1,killswitch-1)
    branch(pen.xcor(),pen.ycor(),newAngle2,changeAngle/2,newLength2,newThiccness2,killswitch-1)
    branch(pen.xcor(),pen.ycor(),newAngle3,changeAngle/2,newLength3,newThiccness3,killswitch-1)
    branch(pen.xcor(),pen.ycor(),newAngle4,changeAngle/2,newLength4,newThiccness4,killswitch-1)
    branch(pen.xcor(),pen.ycor(),newAngle5,changeAngle/2,newLength5,newThiccness5,killswitch-1)
  else:
    pass
    leaf = turtle.Turtle()
    #leaf.shape("circle")
    leaf.color(0,100,0)
    leaf.penup()
    leaf.goto(x,y)
    leaf.pendown()
    leaf.circle(thiccness*5)
    leaf.hideturtle()
branch(0,-180,90,60,100,15,5)
screen.update()





















