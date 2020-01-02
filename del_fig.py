import tkinter

SIZE_OF_ROOT_WINDOWS = '800x600'
WIDTH_OF_CANVAS = 800
HEIGHT_OF_CANVAS = 600
COLOR_OF_CANVAS = 'green'
DELAY = 80


root = tkinter.Tk()
root.geometry(SIZE_OF_ROOT_WINDOWS)
c = tkinter.Canvas(root, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
c.pack()

def p(event):
    print(c.find_overlapping(0, 0, 800, 600))
    print(c.find_all())

def d(event):
    print(c.find_overlapping(0, 0, 800, 600))
    try:
        c.delete(int(event.char))
        print(event.char)
        print(c.find_overlapping(0, 0, 800, 600))
    except:
        print('не число')

def motion():
    root.after(DELAY, motion)

ball1 = c.create_oval(40, 40, 60, 60, fill='green')
ball2 = c.create_oval(140, 140, 160, 160, fill='green')
rect1 = c.create_rectangle(80, 80, 120, 120, fill='lightgreen')
rect2 = c.create_rectangle(180, 180, 220, 220, fill='lightgreen')

root.bind('p', p)
root.bind('<Key>', d)


root.mainloop()
