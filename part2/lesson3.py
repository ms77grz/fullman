from tkinter import Tk, Button
import time

root = Tk()
root.geometry('600x400+500+200')
x = 0

def get_time():
    btn_time['text'] = time.strftime('%X')


def click_counter():
    global x
    x += 1
    root.title(f'You have clicked this button {x} times.')


btn_time = Button(root, text='What time it is?', command=get_time)
btn_time.pack()

btn_cnt = Button(root, text='Click Counter', command=click_counter)
btn_cnt.pack()

root.mainloop()
