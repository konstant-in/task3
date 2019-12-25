import tkinter

# import random

# constants
SIZE_OF_ROOT_WINDOWS = '800x600'
WIDTH_OF_CANVAS = 800
HEIGHT_OF_CANVAS = 600
COLOR_OF_CANVAS = 'green'
DELAY = 80


class Ball():
    def __init__(self, r, x, y, speed_x, speed_y, c):
        self.r = r
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.c = c


# create a window, the canvas and start game
root_of_window = tkinter.Tk()
root_of_window.title("Полёт шаров")
root_of_window.geometry(SIZE_OF_ROOT_WINDOWS)
canvas = tkinter.Canvas(root_of_window, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
canvas.pack()
ball = Ball(20, 0, 0, 10, 20, canvas)
ball.c.create_oval(ball.x, ball.y, ball.x + ball.r, ball.y + ball.r, outline='red', fill='red')
root_of_window.mainloop()
