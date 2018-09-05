import turtle


def init():
    turtle.home()
    turtle.up()


def draw_board():
    turtle.down()
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(200)
    turtle.up()


def draw_block():
    turtle.down()
    turtle.begin_fill()
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(10)
    turtle.end_fill()
    turtle.up()


def draw_square():
    turtle.fillcolor('blue')
    init()
    turtle.down()
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    draw_block()
    draw_block()
    draw_block()


def main():
    init()
    draw_board()
    draw_square()

main()
input("Enter to Exit")