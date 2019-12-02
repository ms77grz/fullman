from tkinter import Tk, Button, Label, Entry
import matplotlib as mpl

root = Tk()

l = Label(root)
l.pack()
e = Entry(root, width=30, justify='center')
e.pack(fill='x')

colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}


def get_color(text_color, hex_color):
    l['text'] = text_color
    e.delete(0, 'end')
    e.insert('end', hex_color)


def make_button(k, v):
    Button(root, bg=k, command=lambda: get_color(k, v)).pack(fill='x')


for k, v in colors.items():
    make_button(k, v)

root.mainloop()
