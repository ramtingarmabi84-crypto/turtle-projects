import turtle
import math

# صفحه
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rose 🌹")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# -------------------------
# گلبرگ
# -------------------------
def petal(radius, angle, color):
    t.color(color)
    t.begin_fill()

    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

    t.end_fill()


# -------------------------
# گلبرگ‌های رز
# -------------------------
t.penup()
t.goto(0, 80)
t.setheading(0)
t.pendown()

colors = ["#8B0000", "#A50000", "#C00000", "#D40000"]

for i in range(18):
    t.setheading(i * 20)
    petal(55, 70, colors[i % len(colors)])

# گلبرگ‌های داخلی
for i in range(12):
    t.setheading(i * 30 + 15)
    petal(35, 80, "#FF0000")

# مرکز گل
t.penup()
t.goto(0, 80)
t.dot(35, "#7A0000")


# -------------------------
# ساقه
# -------------------------
t.goto(0, 65)
t.setheading(-90)
t.color("#228B22")
t.pensize(12)
t.pendown()
t.forward(260)


# -------------------------
# برگ
# -------------------------
def leaf(x, y, heading):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.color("#228B22")
    t.begin_fill()

    for _ in range(2):
        t.circle(45, 60)
        t.left(120)

    t.end_fill()


leaf(0, -40, 25)
leaf(0, -130, 155)

# رگبرگ
t.color("#0B5D1E")
t.pensize(2)

t.penup()
t.goto(0, -40)
t.setheading(25)
t.pendown()
t.forward(35)

t.penup()
t.goto(0, -130)
t.setheading(155)
t.pendown()
t.forward(35)


# -------------------------
# پایان
# -------------------------
turtle.done()