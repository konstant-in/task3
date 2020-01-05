import tkinter

SIZE_OF_ROOT_WINDOWS = '800x600'
WIDTH_OF_CANVAS = 800
HEIGHT_OF_CANVAS = 600
COLOR_OF_CANVAS = 'green'
DELAY = 80

# шар полностью задается парой: canvas, id


def keypress(event):
    print(event.keycode, event)


def motion():
    move_ball(canvas, ball_id, 5, 3)
    root.after(DELAY, motion)


def create_ball(x, y, r, c):
    return c.create_oval(x, y, x + r, y + r, outline='red', fill='red')


def move_ball(c, b, dx, dy):
    c.move(b, dx, dy)


root = tkinter.Tk()
root.title("Полёт шаров")
root.geometry(SIZE_OF_ROOT_WINDOWS)
canvas = tkinter.Canvas(root, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
canvas.pack()

ball_id = create_ball(0, 0, 20, canvas)

root.bind('<Key>', keypress)
motion()

root.mainloop()
