import tkinter

# import random

# constants
SIZE_OF_ROOT_WINDOWS = '800x600'
WIDTH_OF_CANVAS = 800
HEIGHT_OF_CANVAS = 600
COLOR_OF_CANVAS = 'green'
DELAY = 80


def update_of_canvas():
    pppp = canvas.create_oval(140, 140, 160, 160, outline='red', fill='red')
    canvas.bind('<Up>', lambda event: canvas.move(pppp, 0, -2))
    canvas.bind('<Down>', lambda event: canvas.move(pppp, 0, 2))
    canvas.bind('<Left>', lambda event: canvas.move(pppp, -2, 0))
    canvas.bind('<Right>', lambda event: canvas.move(pppp, 2, 0))


def update_of_ball():
    global x0, y0, vx, vy, t
    t = t + DELAY/100
    x = x0 + vx * t
    y = y0 + vy * t + 0.2 * t**2
    print(t, x, y)
    canvas.coords(ball, x, y, x + 40, y + 40)
    root_of_window.after(DELAY, update_of_ball)


# create a window, the canvas and start game
root_of_window = tkinter.Tk()
root_of_window.title("Полёт шаров")
root_of_window.geometry(SIZE_OF_ROOT_WINDOWS)
canvas = tkinter.Canvas(root_of_window, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
print(type(canvas))
canvas.pack()
t = 0
x0 = 0
y0 = 0
vx = 20
vy = 0

ball = canvas.create_oval(x0, y0, x0 + 40, y0 + 40, outline='red', fill='red')

update_of_ball()
root_of_window.mainloop()
