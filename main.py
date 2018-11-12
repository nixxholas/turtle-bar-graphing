# Charlyn Ip Han Qi
# MA7
import sys
# Import the Turtle function
import turtle

class Point:
    label = str
    x = int
    y = int


class Line:
    def __init__(self, Origin, Angle, Destination, Color='black'):
        self.origin = Origin
        self.angle = Angle
        self.color = Color
        self.destination = Destination

    origin = Point
    destination = Point
    angle = int  # Angle in the clockwise direction.
    color = str

    def valid(self):
        return self.destination is Point

class Axis:
    def __init__(self, Origin, XLen, YLen, XLabel, YLabel):
        self.origin = Origin
        self.xlength = XLen
        self.ylength = YLen
        self.xlabel = XLabel
        self.ylabel = YLabel

    origin = Point
    xlength = int
    ylength = int
    xlabel = str
    ylabel = str


class Graph:
    def __init__(self, GraphCore, Data):
        self.graphCore = GraphCore
        self.rawData = Data

    graphCore = Axis
    rawData = str
    data = []


# -	Draw a few closed shapes: triangles, rectangles and shapes of your own design, of different sizes,
# and fill them with colours, especially rectangles, of course, since the bars are rectangular.
def polygon(writer, size, sides, col="black"):
    angle = 360 / sides

    writer.color(col, col)

    writer.begin_fill()

    for count in range(sides):
        writer.forward(size)
        writer.left(angle)

    writer.end_fill()


# Left(num) => Turn anti-clockwise by num(degree)
# Right(num) => Same as Left but clockwise.
# Forward => Move forward

# -	Vary the widths of the lines you draw by using pensize().
# Learn how to use Turtle functions to do some simple drawings. Try these:
# -	Draw a line, using the direction functions like forward(), backward(), right(), left() etc., with appropriate parameters, of course.
# 1 for forward, 2 for backward
def renderline(pencil, distance=0, rotation=0, right=True, direction=1, thickness = 1):
    pencil.pensize(thickness)
    pencil.hideturtle()
    pencil.penup()

    if right:
        pencil.right(rotation)
    elif right is False:
        pencil.left(rotation)
    else:
        return SyntaxError('Invalid rotational direction.')

    pencil.pendown()
    if direction == 1:
        pencil.forward(distance)
    elif direction == 2:
        pencil.backward(distance)
    else:
        return SyntaxError('Invalid direction.')

# The below features can be encased in a function
# -	Draw a line, by specifying coordinates to draw to, using the goto() function, with appropriate control of penup() and pendown().
# -	Draw multiple lines in different directions, connected and not connected. Try drawing lines to write the word “turtle” or any word you choose.
def renderlinebycoords(pencil, line: Line, thickness = 1):
    pencil.hideturtle()
    pencil.penup() # Don't render anything first
    pencil.pensize(thickness)

    pencil.goto(line.origin.x, line.origin.y) # Go to the origin
    pencil.right(line.angle) # rotate properly

    pencil.showturtle()
    pencil.pendown() # let's go
    pencil.goto(line.destination.x, line.destination.y)


# -	Write some text in the picture.

# Step 2 – learn to draw proper diagrams
# A proper diagram is one that has controlled appearances, such as sizes, shapes and colours. Do these exercises:

# -	In the window, plot the axes of a graph which should be perpendicular to each other. You should be able to control the extent of the axes in both directions.
def plotGraph(pencil, zero: Axis, thickness = 1):
    pencil.hideturtle()
    pencil.penup()
    pencil.pensize(thickness)

    pencil.goto(zero.origin.x, zero.origin.y)
    pencil.right(90)

    pencil.pendown()
    pencil.forward(zero.xlength)

    pencil.left(90)
    pencil.forward(zero.ylength)


# -	Label the axes with appropriate text like “distance”, “time”, etc. depending on the need
def labelAxis(pencil):
    pencil.hideturtle()


# -	Learn to place rectangular bars of given sizes where you want them.
def drawBar(pencil, height, label=None, thickness=20, barMargin=10, tickDistance=5):
    pencil.left(90)
    pencil.begin_fill()
    pencil.forward(height)
    pencil.write(str(height))
    pencil.right(90)
    pencil.forward(thickness)
    pencil.right(90)
    pencil.forward(height)
    pencil.left(90)
    pencil.forward(barMargin)
    pencil.end_fill()

    placeTick(pencil, label, tickDistance, thickness)

# -	Place tick marks sensibly at regular intervals along the axes
# -	Label the tick marks with appropriate values
def placeTick(pencil, label: str, height=5, thickness=20):
    # render the tick
    pencil.left(180)
    pencil.forward(thickness/2)
    pencil.left(90)
    pencil.begin_fill()
    pencil.forward(height)
    pencil.end_fill()

    # render the label
    pencil.forward(height / 1.5)
    pencil.right(180)
    pencil.begin_fill() #dk if we really need this...
    pencil.write(label, "center")
    pencil.end_fill()

    pencil.forward((height / 1.5) + height)
    pencil.right(90)
    pencil.forward(thickness/2)


# Find the range of the lengths.
# Divide this range into ten segments, each segment is for 1/10 of the range.
def range(dataset):
    result = {}

    for datum in dataset:
        datumCat = int(datum / 10) #casting this truncates the number

        if result[datumCat] is None:
            result[datumCat] = []
            result[datumCat].append(datum)
        else:
            result[datumCat].append(datum)

    return result


# Count the number of measurements in each range.
def rangeCount(dataset):
    result = {}

    for key in dataset:
        result[key] = len(dataset[key])

    return result


def main():
    arrIndex = 0
    arr = [320, 160]

    # print command line arguments
    for arg in sys.argv[1:]:
        if arrIndex <= len(arr):
            arr[arrIndex] = arg
        arrIndex += 1

    # -	Create a display window of specific size using the setup() function
    window = turtle.Screen()
    window.setup(arr[0], arr[1])

    # call range() to categorize the incoming data
    # call rangeCount() to count the number of items in each range

    # UNDONE - Plot the bar chart for the ten segments. You need to decide what the chart should contain.

    # Leave if clicked
    window.exitonclick()
