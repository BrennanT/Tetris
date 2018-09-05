import turtle


def init():
    """
    Initialize the turtle and put it "up" so we can move it with out drawing.
    """
    turtle.home()
    turtle.up()


def draw_board():
    """
    Draw the 10 block wide, 20 block tall Tetris board.
    """
    turtle.down()
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(100)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.up()


def draw_block():
    """
    Used to draw each block of a shape.
    """
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
    turtle.left(90)
    turtle.up()


def draw_square():
    """
    Draw a Tetris square with the bottom right corner of the default shape at the current turtle position.
    """
    turtle.fillcolor('blue')
    draw_block()
    turtle.fd(10)
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.right(180)
    turtle.fd(10)
    turtle.right(180)
    draw_block()
    turtle.right(90)
    turtle.fd(10)
    turtle.left(90)


def draw_stick():
    """
    Draw a Tetris line with the bottom right corner of the default shape at the current turtle position.
    """
    turtle.fillcolor('yellow')
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.right(90)
    turtle.fd(30)
    turtle.left(90)


def draw_rightshift():
    """
    Draw a "square" with the top two blocks shifted right by one block.
    """
    turtle.fillcolor('purple')
    draw_block()
    turtle.fd(10)
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.fd(10)
    draw_block()
    turtle.right(90)
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(20)
    turtle.right(180)


def draw_leftshift():
    """
    Draw a "square" with the top two blocks shifted left by one block.
    """
    turtle.fillcolor('orange')
    draw_block()
    turtle.fd(10)
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(20)
    turtle.right(180)
    draw_block()
    turtle.fd(10)
    draw_block()
    turtle.right(90)
    turtle.fd(10)
    turtle.left(90)


def draw_tee():
    """
    Draw tee block.
    """
    turtle.fillcolor('red')
    draw_block()
    turtle.fd(10)
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(10)
    turtle.left(90)
    draw_block()
    turtle.right(180)
    turtle.fd(20)
    turtle.right(180)


def draw_l():
    """
    Draw L shaped Tetris block.
    """
    turtle.fillcolor('green')
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.right(90)
    turtle.fd(20)
    turtle.left(90)
    turtle.fd(10)
    draw_block()
    turtle.right(180)
    turtle.fd(10)
    turtle.right(180)


def draw_l_mirrored():
    """
    Draw mirrored L shaped Tetris block.
    """
    turtle.fillcolor('magenta')
    draw_block()
    turtle.fd(10)
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_block()
    turtle.right(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.fd(10)
    turtle.right(180)


def main():
    turtle.speed(11)
    init()
    draw_board()
    draw_l()
    turtle.fd(20)
    draw_square()
    turtle.fd(20)
    draw_tee()
    turtle.fd(30)
    draw_square()
    turtle.left(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(60)
    turtle.left(90)
    draw_l()
    turtle.fd(10)
    turtle.left(90)
    turtle.fd(30)
    draw_leftshift()
    turtle.fd(20)
    draw_rightshift()
    turtle.fd(40)
    turtle.left(90)
    turtle.fd(10)
    draw_l_mirrored()
    turtle.left(90)
    turtle.fd(100)
    turtle.right(180)
    draw_l_mirrored()
    turtle.fd(20)
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    draw_rightshift()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    draw_leftshift()
    turtle.fd(20)
    draw_tee()


main()
turtle.done()
