import tkinter
def keypress(event):
    '''Печать событий клавиатуы

    Печатает:
    state - ражим ввода???
    keysym - символьное обозначение (например: Alt_L, Delete, Control_R)
    keycode - код клавиши
    char - символ клавиши
    x, y - координаты мыши

    '''

    print(event.keycode, event)

root = tkinter.Tk()
root.bind('<Key>',keypress )
# первый параметр
# keycode
# 'char'
# <'keysym'>
root.mainloop()
