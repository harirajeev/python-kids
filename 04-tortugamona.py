import turtle

t = turtle.Pen()

#rectangle
t.reset()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.reset()
for i in range(1, 5):
    t.forward(50)
    t.left(90)

#hexagon
t.reset()
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)

t.reset()
for i in range(1, 7):
    t.forward(50)
    t.left(60)

#triangle
t.reset()
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)

t.reset()
for i in range(1, 4):
    t.forward(50)
    t.left(120)

#dots
t.reset()
t.forward(10)
t.up()
t.forward(10)
t.down()
t.forward(10)
t.up()
t.forward(10)
t.down()
t.forward(10)
t.up()
t.forward(10)
t.down()
t.forward(10)
t.up()
t.forward(10)
t.down()
t.forward(10)
t.up()
t.forward(10)
t.down()
t.forward(10)
t.up()
t.forward(10)
t.down()
t.forward(10)
t.up()
t.forward(10)
t.down()

t.reset()
for i in range(1, 11):
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()

# generic
l=20
s=20
g=360/l
t.reset()
for i in range(1, l + 1):
    t.forward(s)
    t.left(g)

# all the poligons
for p in range(3,25):
    l=p
    s=50*2/p
    g=360/l
    t.reset()
    for i in range(1, l + 1):
        t.forward(s)
        t.left(g)
