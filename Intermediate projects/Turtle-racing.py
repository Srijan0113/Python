import turtle
import time
import random

WIDTH , HEIGHT= 500,500
COLORS=['red','orange','blue','yellow','black','cyan','green','purple','pink','brown']

def get_number_of_racers():
    racers=0
    while True:
        racers=input("Enter the number of racers (2-10) : " )
        if racers.isdigit():
            racers=int(racers)
        else:
            print("Invalid input !!! ")
            continue
        if 2<= racers<= 10:
            return racers
        else:
            print("Number is not in range 2-10. Try again ")

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)
            x,y = racer.pos()
            if y>= HEIGHT//2 - 10:
                return colors[turtles.index(racer)] #function stops

# ['blue','red']
# [racer1, racer2] ---- list of turtles
# 0           1

def create_turtles(colors):
    turtles=[]
    spacingx = WIDTH// (len(colors)+1)
    for i,color in enumerate(colors): #enumerate gives the index with color
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) #in default they are turned to right so left 90 degree will turn them to upward direction
        turtles.append(racer)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx, -HEIGHT//2 + 20 )
        racer.pendown()
    return turtles




def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing ! ")

racers=get_number_of_racers()
print(f"No. of Racers = {racers}")
init_turtle()
colors=COLORS[:racers]
winner=race(colors)
print("The winner of the race is the turtle with color",winner)
time.sleep(7) #to see which turtle won



# racer=turtle.Turtle()
# racer.speed(1)
# racer.penup() #no line is drawn
# racer.speed('turtle')
# racer.color('cyan')
# racer.forward(100) #distance
# racer.left(90) #angle
# racer.pendown() #starts drawing line
# racer.forward(100)
# racer.right(100)
# racer.backward(100)
# time.sleep(20)


