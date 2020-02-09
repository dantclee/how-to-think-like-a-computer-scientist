import turtle
bcolor = input("Background color: ")
tcolor = input("Turtle color: ")
window = turtle.Screen()
#window.bgcolor("lightgreen")
window.bgcolor(bcolor) # Set the window background color
window.title("Hello, Tess!") # Set the window title

tess = turtle.Turtle()
tess.color(tcolor) # Tell tess to change her color
tess.pensize(3) # Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)
window.mainloop()
