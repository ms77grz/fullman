from tkinter import Tk, Button, Label, Entry

root = Tk()

colors = {
    '#ff0000': 'Красный',
    '#ff7d00': 'Оранжевый',
    '#ffff00': 'Желтый',
    '#00ff00': 'Зеленый',
    '#007dff': 'Голубой',
    '#0000ff': 'Синий',
    '#7d00ff': 'Фиолетовый',
}


class ColorButton(object):
    def __init__(self, master, text_color, hex_color):
        self.master = master
        self.text_color = text_color
        self.hex_color = hex_color
        self.button = Button(self.master, bg=self.hex_color,
                             command=self.get_color)
        self.button.pack(fill='x')

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, 'end')
        e.insert('end', self.hex_color)


l = Label(root)
l.pack()
e = Entry(root, width=30, justify='center')
e.pack()

for hex_color, text_color in colors.items():
    ColorButton(root, text_color, hex_color)

root.mainloop()
