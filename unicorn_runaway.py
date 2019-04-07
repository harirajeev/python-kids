import time
from tkinter import *

# create canvas
tk = Tk()
canvas = Canvas(tk, width=800, height=600)
canvas.pack()
# draw pony
pony = PhotoImage(file="pony.gif")
canvas.create_image(0, 0, anchor=NW, image=pony)
# pony runaway
for x in range(0, 100):
    canvas.move(1, 8, 0)
    tk.update()
    time.sleep(0.05)

tk.mainloop()
