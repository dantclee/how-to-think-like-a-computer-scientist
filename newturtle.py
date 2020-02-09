import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup() # This is new
size = 20
for _ in range(30):
    tess.stamp() # Leave an impression on the canvas
    size = size + 3 # Increase the size on every iteration
    tess.forward(size) # Move tess along
    tess.right(24) # ... and turn her

tess.color("red")

window.mainloop()
