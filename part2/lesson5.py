from tkinter import Tk, Entry, Label, Button
# from functools import partial

root = Tk()
root.geometry('600x400+500+200')


def add_text(text):
    e.insert('end', text)


def del_text():
    e.delete(0, 'end')


def get_text():
    l_text['text'] = e.get()


l = Label(root, text='Поле ввода')
l.pack()

e = Entry(root)
e.insert('end', 'Hello')
e.insert('end', ' world!')
e.pack()

l_pass = Label(root, text='Введите пароль')
l_pass.pack()

e_pass = Entry(root,show='*')
e_pass.pack()

b = Button(root, text='Enter')
b.pack()

# b_add = Button(root, text='Add', command=partial(add_text,'caramba'))
b_add = Button(root, text='Add', command=lambda : add_text('caramba!!!'))
b_add.pack()


b_del = Button(root, text='Delete', command=del_text)
b_del.pack()

b_get = Button(root, text='Get', command=get_text)
b_get.pack()

l_text = Label(root, bg='red', fg='white')
l_text.pack(fill='x')

root.mainloop()
