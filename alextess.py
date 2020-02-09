import turtle
window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")
window.title("Tess & Alex")

tess = turtle.Turtle() # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle() # Create alex

for _ in range(3): # Make tess draw equilateral triangle
    tess.forward(80)
    tess.left(120)

tess.right(180) # Turn tess around
tess.forward(80) # Move her away from the origin

for _ in range(4):  # Make alex draw a square
    alex.forward(50)
    alex.left(90)

window.mainloop()
