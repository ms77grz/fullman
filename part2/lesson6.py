from tkinter import Tk, Button, Label, Entry
import matplotlib as mpl

root = Tk()

colors = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')


def make_color_button(color):
    return Button(root, bg=color, command=lambda: get_color(color)).pack(fill='x')


def get_color(color):
    top_label['text'] = color.upper()
    top_entry.delete(0, 'end')
    top_entry.insert('end', mpl.colors.cnames[color])


top_label = Label(root)
top_label.pack()

top_entry = Entry(root, width=30, justify='center')
top_entry.pack()

for color in colors:
    make_color_button(color)

root.mainloop()
