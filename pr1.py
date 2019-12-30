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


class App():
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.title("Управление шаром")
        self.root_window.geometry(SIZE_OF_ROOT_WINDOWS)
        self.create_world()
        self.root_window.mainloop()  # Метод mainloop() объекта Tk запускает главный цикл обработки событий,

    def create_world(self):
        """Эта функция создает полотно,
        а на нем шар который перемещается стрелками клавиатуры.
        Клавиша «p» распечатывает текущие координаты
        левого верхнего и правого нижнего угла описывающего круг квадрата.
        Клавиша «Home» возвращает шар в левый верхний угол
        Клавиша Delete удаляет шар
        """
        # def creat_battlefield()

        self.canvas = tkinter.Canvas(self.root_window, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
        self.canvas.pack()
        self.canvas.focus_set()

        # Пивязываем события
        # Не зависящие от наличия шара
        def mouse_click(event):
            print("Клик по координатам:", event.x, event.y)

        # Создаем шар
        ball = self.canvas.create_oval(0, 0, R, R, outline='red', fill='red')

        # Управление шара
        def to_home(event):
            self.canvas.coords(ball, 0, 0, R, R)
            print("Возвращаю шар в «Домой»")

        self.canvas.bind('<Up>', lambda event: self.canvas.move(ball, 0, -2))
        self.canvas.bind('<Down>', lambda event: self.canvas.move(ball, 0, 2))
        self.canvas.bind('<Left>', lambda event: self.canvas.move(ball, -2, 0))
        self.canvas.bind('<Right>', lambda event: self.canvas.move(ball, 2, 0))
        self.canvas.bind('p', lambda event: print(self.canvas.coords(ball)))
        self.canvas.bind('<Delete>', lambda event: self.canvas.delete(ball))
        self.canvas.bind('<Home>', to_home)
        self.canvas.bind('<Button-1>', mouse_click)


app = App()