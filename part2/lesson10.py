from tkinter import Tk, Button, Frame

root = Tk()
root.geometry('600x400+500+200')

main_frame = Frame(root)
main_frame.pack()

btns = [7, 8, 9, 4, 5, 6, 1, 2, 3, 0]
row = 0
column = 0

for btn in btns:
    if btn == 0:
        Button(main_frame, text=btn, padx=10, pady=5).grid(
            row=row, columnspan=3)
    else:
        Button(main_frame, text=btn, padx=10, pady=5).grid(
            row=row, column=column)
    column += 1
    if column == 3:
        row += 1
        column = 0


root.mainloop()
