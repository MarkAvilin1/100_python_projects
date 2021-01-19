# with open("words.csv", "r") as file:
#     data = file.readlines()
#     english = []
#     for i in range(len(data)):
#         english.append(data[i].split(",")[1])
#     with open("en.txt", "w") as w:
#         for i in english:
#             w.write(str(i))

from tkinter import *


window = Tk()
img = PhotoImage(file="card_front.png")
window.config(padx=50, pady=50, bg="cyan")

canvas = Canvas(width=800, height=256)
canvas.create_image(400, 268, image=img)
canvas.pack()


window.mainloop()

