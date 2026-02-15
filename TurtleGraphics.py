#TurtleGraphics.py
#Name:
#Date:
#Assignment:

def drawSquare(DJ, size):
    for i in range(4):
        DJ.forward(size)
        DJ.right(90)


def fillTopRight(DJ, size):
    
    drawSquare(DJ, size)

   
    DJ.penup()
    DJ.goto(-170, -30)         
    DJ.forward(size)        
    DJ.left(90)
    DJ.forward(size)      
    DJ.right(180)           
    DJ.pendown()

    
    DJ.color("blue")
    DJ.begin_fill()
    drawSquare(DJ, size/2)
    DJ.end_fill()


def squaresInSquares(DJ, size, count):
    for i in range(count):
        drawSquare(DJ, size)

       
        DJ.penup()
        DJ.forward(10)
        DJ.right(90)
        DJ.forward(10)
        DJ.left(90)
        DJ.pendown()

        size -= 20

def main():
    t = turtle.Turtle()
    t.speed(20)   

    
    t.penup()
    t.goto(-170, 170)
    t.setheading(0)
    t.pendown()

    fillTopRight(t, 200)

   
    t.penup()
    t.goto(30, -40)
    t.setheading(0)
    t.pendown()

    squaresInSquares(t, 150, 7)

main()
