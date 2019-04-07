import time
from tkinter import *

def movePony(event):
    step = 5
    if event.keysym == "Up":
        canvas.move(imageID, 0, -step)
    elif event.keysym == "Down":
        canvas.move(imageID, 0, step)
    elif event.keysym == "Left":
        canvas.move(imageID, -step , 0)
    elif event.keysym == "Right":
        canvas.move(imageID, step, 0)
    else:
        print("Unknown event")

tk = Tk()
canvas = Canvas(tk, width=800, height=600)
canvas.pack()
pony = PhotoImage(file="pony.gif")
imageID = canvas.create_image(0, 0, anchor=NW, image=pony)

canvas.bind_all("<KeyPress-Up>", movePony)
canvas.bind_all("<KeyPress-Down>", movePony)
canvas.bind_all("<KeyPress-Left>", movePony)
canvas.bind_all("<KeyPress-Right>", movePony)

tk.mainloop()
