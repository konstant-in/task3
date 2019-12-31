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

def motion():
    canvas.move(target, VX2, VY2)
    if g_fire:
        canvas.move(ball_of_gun, VX1, VY1)
    if len(canvas.coords(ball_of_gun)) > 0 and target in canvas.find_overlapping(*canvas.coords(ball_of_gun)):
        print("Попал!!!")
        canvas.delete(target)
        canvas.delete(ball_of_gun)
    if len(canvas.coords(ball_of_gun)) > 0 and canvas.coords(ball_of_gun)[2] > WIDTH_OF_CANVAS:
        print('Ядро улетело!')
        canvas.delete(ball_of_gun)
    if len(canvas.coords(target)) > 0 and canvas.coords(target)[3] < 0:
        print('Цель улетела!')
        canvas.delete(target)
    if len(canvas.coords(ball_of_gun)) == len(canvas.coords(target)) == 0:
        print('Нет ни ядер, ни целей')
        game_init()
    root_window.after(DELAY, motion)

ball_of_gun = None
target = None

def game_init():
    global ball_of_gun, target, g_fire
    g_fire = False
    print('Начинаем новую игру')
    ball_of_gun = canvas.create_oval(0, HEIGHT_OF_CANVAS / 2, R, HEIGHT_OF_CANVAS / 2 + R, outline='red', fill='red')
    target = canvas.create_oval(WIDTH_OF_CANVAS - R2, HEIGHT_OF_CANVAS, WIDTH_OF_CANVAS, HEIGHT_OF_CANVAS - R2, outline='blue', fill='blue', tag='ball2')

root_window = tkinter.Tk()
root_window.title("Пушка стреляющяя ядрами")
root_window.geometry(SIZE_OF_ROOT_WINDOWS)
canvas = tkinter.Canvas(root_window, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
canvas.pack()
canvas.focus_set()
canvas.bind('<Up>', lambda event: canvas.move(ball_of_gun, 0, -10))
canvas.bind('<Down>', lambda event: canvas.move(ball_of_gun, 0, 10))
canvas.bind('<Home>', lambda event: canvas.coords(ball_of_gun, 0, HEIGHT_OF_CANVAS / 2, R, HEIGHT_OF_CANVAS / 2 + R))
canvas.bind('<space>', lambda event: to_fire())

game_init()

motion()
root_window.mainloop()
