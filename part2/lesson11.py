from tkinter import Tk, Button, Label, Entry

root = Tk()
root.geometry('600x400+500+200')

l_login = Label(root, text='Login')
l_login.grid(row=0, column=0)

e_login = Entry(root)
e_login.grid(row=0,column=1)

l_password = Label(root, text='Password')
l_password.grid(row=1, column=0)

e_password = Entry(root)
e_password.grid(row=1,column=1)

b_login = Button(root, text='Enter')
b_login.grid(row=2,column=0)

b_register = Button(root, text='Register')
b_register.grid(row=2,column=1)

b_forgot = Button(root, text='Forgot password?')
b_forgot.grid(row=2, column=2)

root.mainloop()