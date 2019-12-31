import tkinter
import random

# constants
SIZE_OF_ROOT_WINDOWS = '800x600'
WIDTH_OF_CANVAS = 800
HEIGHT_OF_CANVAS = 600
COLOR_OF_CANVAS = 'green'
DELAY = 40
R = 20
R2 = 60
VX1 = 10
VY1 = 0
VX2 = 0
VY2 = -1

g_fire = False


def to_fire():
    global g_fire
    g_fire = True


def del_ball2(event):
    print("Попал!!!")
    canvas.delete(target)


def motion():
    if g_fire:
        canvas.move(ball_of_gun, VX1, VY1)
    if target in canvas.find_overlapping(*canvas.coords(ball_of_gun)):
        print("Попал!!!")
        canvas.delete(target)

    canvas.move(target, VX2, VY2)
    root_window.after(DELAY, motion)


root_window = tkinter.Tk()
root_window.title("Пушка стреляющяя ядрами")
root_window.geometry(SIZE_OF_ROOT_WINDOWS)
canvas = tkinter.Canvas(root_window, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
canvas.pack()
ball_of_gun = canvas.create_oval(0, HEIGHT_OF_CANVAS / 2, R, HEIGHT_OF_CANVAS / 2 + R, outline='red', fill='red')
target = canvas.create_oval(WIDTH_OF_CANVAS - R2, HEIGHT_OF_CANVAS, WIDTH_OF_CANVAS, HEIGHT_OF_CANVAS - R2, outline='blue', fill='blue', tag='ball2')

canvas.focus_set()
canvas.bind('<Up>', lambda event: canvas.move(ball_of_gun, 0, -10))
canvas.bind('<Down>', lambda event: canvas.move(ball_of_gun, 0, 10))
canvas.bind('<Home>', lambda event: canvas.coords(ball_of_gun, 0, HEIGHT_OF_CANVAS / 2, R, HEIGHT_OF_CANVAS / 2 + R))
canvas.bind('<space>', lambda event: to_fire())

canvas.tag_bind('ball2', '<Button-1>', del_ball2)

motion()
root_window.mainloop()
