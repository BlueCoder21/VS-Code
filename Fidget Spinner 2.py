from turtle import *
state = {"turn":0}
def spin():
    clear()
    angle = state["turn"] / 10
    right(angle)
    forward(100)
    dot(80,"red")
    back(100)
    
    right(72)
    forward(100)
    dot(80,"green")
    back(100)
    
    right(72)
    forward(100)
    dot(80,"blue")
    back(100)
    
    right(72)
    forward(100)
    dot(80,"orange")
    back(100)
    
    right(72)
    forward(100)
    dot(80,"yellow")
    back(100)
    
    right(72)
    update()

def animate():
    if state["turn"]>0:
        state["turn"]-=1 #turn = turn - 1
    spin()
    ontimer(animate,20)

def flick():
    state["turn"]+=10

setup(420,420,370,0)
hideturtle()
tracer(False)
width(20)
onkey(flick,"space")
listen()
animate()
done()