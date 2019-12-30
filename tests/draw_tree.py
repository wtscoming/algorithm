from turtle import *

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 20, t)
        t.left(40)
        tree(branch_len - 20, t)
        t.right(20)
        t.backward(branch_len)

if __name__ == '__main__':
    t = Turtle()
    my_win = t.getscreen()
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color('green')
    tree(80, t)
    my_win.exitonclick()
