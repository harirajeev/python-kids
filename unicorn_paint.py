import time
from tkinter import *

# move the pony
def movePony(event):
    global x, y, imageID
    oldX = x
    oldY = y
    step = 10
    if event.keysym == "Up":
        canvas.move(imageID, 0, -step)
        y = y - step
    elif event.keysym == "Down":
        canvas.move(imageID, 0, step)
        y = y + step
    elif event.keysym == "Left":
        canvas.move(imageID, -step , 0)
        x = x - step
    elif event.keysym == "Right":
        canvas.move(imageID, step, 0)
        x = x + step
    else:
        print("Unknown event")
    canvas.create_line(oldX, oldY, x, y)

# create canvas
tk = Tk()
canvas = Canvas(tk, width=800, height=600)
canvas.pack()
# draw pony
pony = PhotoImage(file="pony.gif")
x = 100
y = 100
imageID = canvas.create_image(x, y, image=pony)

# capture key press
canvas.bind_all("<KeyPress-Up>", movePony)
canvas.bind_all("<KeyPress-Down>", movePony)
canvas.bind_all("<KeyPress-Left>", movePony)
canvas.bind_all("<KeyPress-Right>", movePony)

tk.mainloop()
