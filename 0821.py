import turtle

turtle.color('yellow')
turtle.hideturtle()

# n 要大于 2

def draw_polygon(n):
  for i in range(n):
    turtle.forward(200)
    turtle.right(144)


turtle.begin_fill()
draw_polygon(5)
turtle.end_fill()

