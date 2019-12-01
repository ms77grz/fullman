from tkinter import Tk, Button, Label, PhotoImage

root = Tk()
root.geometry('600x400+500+200')

l = Label(root, text='The Main Line 1\nLine 2\nLine 3\nLine 4\nLine 5',
          font=('Comic Sans MS', 10, 'bold'),
          bg='#21c056', fg='#ef253c', justify='right',
          width=50, height=10, anchor='se')
l.pack()

img = PhotoImage(file='py-logo.png')

l_logo = Label(root, image=img)
l_logo.pack()

root.mainloop()
