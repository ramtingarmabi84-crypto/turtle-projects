import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pink Rose 🌹")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# -------------------------
# ساخت گلبرگ
# -------------------------
def petal(size, color):
    t.color(color)
    t.begin_fill()

    for _ in range(2):
        t.circle(size, 70)
        t.left(110)

    t.end_fill()


# -------------------------
# گلبرگ‌های بزرگ بیرونی
# -------------------------
t.penup()
t.goto(0, 80)
t.pendown()

pink_colors = [
    "#FF69B4",
    "#FF5FA2",
    "#FF85C1",
    "#FF4F9A"
]

for i in range(16):
    t.setheading(i * 22.5)
    petal(90, pink_colors[i % len(pink_colors)])


# -------------------------
# گلبرگ‌های داخلی
# -------------------------
for i in range(12):
    t.setheading(i * 30 + 10)
    petal(60, "#FF69B4")


# -------------------------
# مرکز گل
# -------------------------
t.penup()
t.goto(0, 80)
t.dot(45, "#E83E8C")


# -------------------------
# ساقه
# -------------------------
t.goto(0, 60)
t.setheading(-90)
t.color("#228B22")
t.pensize(12)
t.pendown()
t.forward(280)


# -------------------------
# برگ‌ها
# -------------------------
def leaf(x, y, direction):
    t.penup()
    t.goto(x, y)
    t.setheading(direction)
    t.color("#228B22")
    t.begin_fill()

    for _ in range(2):
        t.circle(50, 60)
        t.left(120)

    t.end_fill()


leaf(0, -30, 25)
leaf(0, -140, 155)

turtle.done()