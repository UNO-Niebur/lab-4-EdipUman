#TurtleGraphics.py
#Name:Edip Uman
#Date: 2/25/26
#Assignment: Lab 4

def drawSquare(DJ, size):
    for i in range(4):
        DJ.forward(size)
        DJ.right(90)
        
def drawPolygon(DJ, sides, size):
    DJ.clear()
    DJ.penup()
    DJ.goto(0, 0) 
    DJ.setheading(0)
    DJ.pendown()

    for _ in range(sides):
        DJ.forward(size)
        DJ.right(360 / sides)


def fillTopRight(DJ, size):
    DJ.clear()

   
    DJ.penup()
    DJ.goto(-size/2, size/2)
    DJ.setheading(0)
    DJ.pendown()
    drawSquare(DJ, size)

   
    DJ.penup()
    DJ.goto(0, size/2)
    DJ.setheading(0)
    DJ.pendown()

    DJ.color("blue")
    DJ.begin_fill()
    drawSquare(DJ, size/2)
    DJ.end_fill()


def squaresInSquares(DJ, size, count):
    DJ.clear()

    for i in range(count):
        DJ.penup()
        DJ.goto(-size/2, size/2)
        DJ.setheading(0)
        DJ.pendown()

        drawSquare(DJ, size)

        size -= 20

def main():
    DJ = turtle.Turtle()
    DJ.speed(5) 

    
    fillTopRight(DJ, 200)

    
    DJ.penup()
    DJ.goto(200, 0)
    DJ.setheading(0)
    DJ.pendown()

    squaresInSquares(DJ, 150, 7)
    
    DJ.penup()
    DJ.goto(-200, -150)
    DJ.setheading(0)
    DJ.pendown()
    drawPolygon(DJ, sides=6, size=100)



main()


 
