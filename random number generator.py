from tkinter import Tk, Label
import random

root = Tk()
label = Label(root)
root.resizable = False

label.pack()

def replace_text():
    label.config(text=str(random.random()))
    root.after(1000, replace_text)

replace_text()
root.mainloop()
