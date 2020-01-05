import tkinter
import random

# constants
SIZE_OF_ROOT_WINDOWS = '800x600'
WIDTH_OF_CANVAS = 800
HEIGHT_OF_CANVAS = 600
COLOR_OF_CANVAS = 'green'
DELAY = 40

# радиусы ядра и цели
R1 = 20
R2 = 60

# начальные координаты ядра и цели
X1 = 0
Y1 = HEIGHT_OF_CANVAS / 2
X2 = WIDTH_OF_CANVAS - R2
Y2 = HEIGHT_OF_CANVAS
# скорости ядра и цели
VX1 = 10
VY1 = 0
VX2 = 0
VY2 = -1

FIRE = False


def to_fire():
    global FIRE
    FIRE = True


def exsist_ball(b):
    # шар существует, если длина списка его координат больше нуля
    return len(canvas.coords(b)) != 0


def motion():
    global ball_of_gun, target
    if not exsist_ball(ball_of_gun):
        ball_of_gun = create_ball(X1, Y1, R1)
    if not exsist_ball(target):
        target = create_target(X2, Y2, R2)
    if FIRE:
        canvas.move(ball_of_gun, VX1, VY1)
    canvas.move(target, VX2, VY2)
    if exsist_ball(ball_of_gun) and target in canvas.find_overlapping(*canvas.coords(ball_of_gun)):
        print("Попал!!!")
        canvas.delete(target)
        canvas.delete(ball_of_gun)
    if exsist_ball(ball_of_gun) and canvas.coords(ball_of_gun)[2] > WIDTH_OF_CANVAS:
        print('Ядро улетело!')
        canvas.delete(ball_of_gun)
    if exsist_ball(target) and canvas.coords(target)[3] < 0:
        print('Цель улетела!')
        canvas.delete(target)
    root_window.after(DELAY, motion)


def create_ball(x, y, r):
    global FIRE
    FIRE = False
    print('Новое ядро')
    return canvas.create_oval(x, y, r, y + r, outline='red', fill='red')


def create_target(x, y, r):
    print('Новая цель')
    return canvas.create_oval(x, y, x + r, y - r, outline='blue', fill='blue', tag='ball2')


root_window = tkinter.Tk()
root_window.title("Пушка стреляющяя ядрами")
root_window.geometry(SIZE_OF_ROOT_WINDOWS)
canvas = tkinter.Canvas(root_window, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
canvas.pack()
canvas.focus_set()
canvas.bind('<Up>', lambda event: canvas.move(ball_of_gun, 0, -10))
canvas.bind('<Down>', lambda event: canvas.move(ball_of_gun, 0, 10))
canvas.bind('<Home>', lambda event: canvas.coords(ball_of_gun, 0, HEIGHT_OF_CANVAS / 2, R1, HEIGHT_OF_CANVAS / 2 + R1))
canvas.bind('<space>', lambda event: to_fire())

ball_of_gun = create_ball(X1, Y1, R1)

target = create_target(X2, Y2, R2)

motion()
root_window.mainloop()
