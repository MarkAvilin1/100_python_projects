from tkinter import *


def converter():
    d = round(float(mile.get()) * 1.60934)
    km.config(text=d)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

title = Label(text="Is equal to", font=("Arial", 20))
title.grid(column=0, row=1)

mile = Entry(width=8, font=("Arial", 20))
mile.focus()
mile.grid(column=1, row=0)

mile_title = Label(text="Miles", font=("Arial", 20))
mile_title.grid(column=2, row=0)

km = Label(text="0", font=("Arial", 20))
km.grid(column=1, row=1)

km_title = Label(text="Km", font=("Arial", 20))
km_title.grid(column=2, row=1)

button = Button(text="Convert", width=8, command=converter, font=("Arial", 20))
button.grid(column=1, row=2)
window.mainloop()
