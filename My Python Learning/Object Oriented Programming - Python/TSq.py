from turtle import Turtle
import turtle
def drawSquare(t, x, y, length):
    t.up()
    t.goto(x,y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)
def main():
    x = int(input("Enter the X coordinate of the corner point: "))
    y = int(input("Enter the Y coordinate of the corner point: "))
    length = int(input("Enter the length of the sides length: "))
    drawSquare(Turtle(), x, y, length)
if __name__ == "__main__":
    main()
turtle.done()

