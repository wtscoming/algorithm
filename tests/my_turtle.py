from turtle import *

my_turtle = Turtle()
my_win = my_turtle.getscreen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 10)

if __name__ == '__main__':
    draw_spiral(my_turtle, 200)
    my_win.exitonclick()
