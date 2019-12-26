# Исполльзавал информацию с:
# https://younglinux.info/tkinter/canvasmeth.php
import tkinter

# import random

# constants
SIZE_OF_ROOT_WINDOWS = '800x600'
WIDTH_OF_CANVAS = 800
HEIGHT_OF_CANVAS = 600
COLOR_OF_CANVAS = 'green'
DELAY = 40
R = 20


def create_world():
    """Эта функция создает полотно,
    а на нем шар который перемещается стрелками клавиатуры.
    Клавиша «p» распечатывает текущие координаты
    левого верхнего и правого нижнего угла описывающего круг квадрата.
    Клавиша «Home» возвращает шар в левый верхний угол
    Клавиша Delete удаляет шар

    Второй шар перемещается, пока не достигнет правой стороны поля
    """
    canvas = tkinter.Canvas(root_window, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
    canvas.pack()
    ball = canvas.create_oval(0, 0, R, R, outline='red', fill='red')
    canvas.focus_set()
    canvas.bind('<Up>', lambda event: canvas.move(ball, 0, -2))
    canvas.bind('<Down>', lambda event: canvas.move(ball, 0, 2))
    canvas.bind('<Left>', lambda event: canvas.move(ball, -2, 0))
    canvas.bind('<Right>', lambda event: canvas.move(ball, 2, 0))
    canvas.bind('p', lambda event: print(canvas.coords(ball)))
    canvas.bind('<Delete>', lambda event: canvas.delete(ball))
    canvas.bind()

    def to_home(event):
        canvas.coords(ball, 0, 0, R, R)
        print("Возвращаю шар в «Домой»")

    canvas.bind('<Home>', to_home)

    ball2 = canvas.create_oval(40, 40, 40 + R, 40 + R, outline='blue', fill='blue')

    def mouse_click(event):
        print("Клик по координатам:", event.x, event.y)

    canvas.bind('<Button-1>', mouse_click)

    def del_ball2(event):
        print("Попал по ball2")
        canvas.delete(ball2)

    canvas.tag_bind(ball2, '<Button-1>', del_ball2)

    def motion():
        """
        Бесконечный цикл блокирует обновление графического интерфейса (если он выполняется не в отдельном потоке).
        Вместо него лучше использовать метод after.
        Другой вариант - в цикле явно вызывать root_window.update() для обновления интерфейса.
        """
        try:
            # print("Текущие координаты ball2:", canvas.coords(ball2)[2], canvas.coords(ball2)[3])
            canvas.move(ball2, 2, 1)
            if canvas.coords(ball2)[2] < WIDTH_OF_CANVAS:
                root_window.after(DELAY, motion)
        except:
            pass

    motion()


# create a window, the canvas and start game
root_window = tkinter.Tk()
root_window.title("Полёт шаров")
root_window.geometry(SIZE_OF_ROOT_WINDOWS)
b = tkinter.Button(root_window, text="Кнопка")
b.pack()
create_world()
root_window.mainloop()
