import tkinter

# Заготовка ??????????????????????????

# constants
SIZE_OF_ROOT_WINDOWS = '800x600'
WIDTH_OF_CANVAS = 800
HEIGHT_OF_CANVAS = 600
COLOR_OF_CANVAS = 'green'
DELAY = 80


class Ball():
    def __init__(self, x, y, radius, canvas):
        self.x = x
        self.y = y
        self.radius = radius
        self.canvas = canvas
        self.wiev_ball = self.canvas.create_oval(self.x,
                                                 self.y,
                                                 self.x + self.radius,
                                                 self.y + self.radius,
                                                 outline='red',
                                                 fill='red')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.wiev_ball, dx, dy)


def keypress(event):
    print(event.keycode, event)


def motion():
    b.move(5, 3)
    print(b.x, b.y)
    root.after(DELAY, motion)


def move_ball(ball, dx, dy):
    canvas.move(ball.wiev_ball, dx, dy)


# create a window, the canvas and start game
root = tkinter.Tk()
root.title("Полёт шаров")
root.geometry(SIZE_OF_ROOT_WINDOWS)
canvas = tkinter.Canvas(root, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
canvas.pack()

b = Ball(0, 0, 20, canvas)

root.bind('<Key>', keypress)
motion()

root.mainloop()
