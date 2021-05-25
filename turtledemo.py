import turtle
import time

turtle.forward(150)     # moves the turtle 150 units forward
turtle.right(90)        # rotates the turtle 90 degree right
turtle.forward(150)     # moves the turtle 150 units forward
turtle.circle(50)

turtle.done()           # keeps the screen/whiteboard awake till we close it ourselves
#time.sleep(4)          # keeps the screen/whiteboard awake for 4 seconds before it closes
done = "Well done, you hvae completed the drawing."
print(done)