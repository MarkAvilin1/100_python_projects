from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def on_click1():
    my_label.config(text=inputs.get())


def on_click2():
    my_label.config(text="I'm Mark, from Earth")


my_label = Label(text="I'm Mark, from Earth")
my_label.grid(column=0, row=0)

button1 = Button(text="Click here", command=on_click1)
button1.grid(column=1, row=1)

button2 = Button(text="Click here", command=on_click2)
button2.grid(column=2, row=0)

inputs = Entry()
inputs.grid(column=3, row=2)

window.mainloop()
