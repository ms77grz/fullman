from tkinter import Tk

root = Tk()
root.title('Mega GUI app')
root.iconbitmap('cherry.ico')
root.geometry('600x400+500+200')
root.resizable(0, 0)
root.config(bg='#5e6473')
root['bg'] = '#333'

root.mainloop()
