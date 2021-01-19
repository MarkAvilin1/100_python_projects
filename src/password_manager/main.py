from tkinter import *
from tkinter import messagebox
# from password_generator import PasswordGenerator
import json
import random

BACKGROUND = "#E9FAFF"


# ---------------------------- Search ------------------------------- #

def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(website.get(), f"Email: {data[website.get()]['email']}"
                                               f"\nPassword: {data[website.get()]['password']}")
    except FileNotFoundError as file:
        messagebox.showinfo(f"{file} does not exist!")
    except KeyError:
        messagebox.showinfo(website.get(), f"The {website.get()}, does not found!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generator():
    password.delete(0, END)
    b_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    rand_b_letters = [random.choice(b_letters) for _ in range(2)]
    s_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    rand_s_letters = [random.choice(s_letters) for _ in range(4)]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    nums = [random.choice(numbers) for _ in range(1)]
    symbols = ["*", "/", "_", "&", "#", "@", "=", "%", "$", "!"]
    signs = [random.choice(symbols) for _ in range(1)]

    new_pass = rand_b_letters + signs + rand_s_letters + nums
    random.shuffle(new_pass)
    gen_password = "".join(new_pass)

    # pwo = PasswordGenerator()
    password.insert(0, gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    w = website.get()
    e = email.get()
    p = password.get()
    new_data = {
        w: {
            "email": e,
            "password": p
        }
    }

    if len(w) or len(e) or len(p) != 0:
        is_ok = messagebox.askquestion(title=w, message=f"""These are the details entered
    Email: {e}
    Password: {p}
    Is it ok to save?""")

        if is_ok:
            # with open("password_manager.txt", "a") as line:
            try:
                with open("data.json", "r") as data_file:
                    # line.write(f"\n{w} | {e} | {p}")
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website.delete(0, END)
                email.delete(0, END)
                password.delete(0, END)
                messagebox.showinfo(title=website.get(), message="The data had saved successfully!")
    else:
        messagebox.showinfo(title="Error!", message="Should fill all field!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", bg=BACKGROUND)
website_label.grid(column=0, row=1, sticky=E)

website = Entry(width=30)
website.focus()
website.grid(column=1, row=1)

search_btn = Button(text="Search", width=14, command=search)
search_btn.grid(column=2, row=1)

email_label = Label(text="Email/Username: ", bg=BACKGROUND)
email_label.grid(column=0, row=2, sticky=E)

email = Entry(width=48)
email.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ", bg=BACKGROUND)
password_label.grid(column=0, row=3, sticky=E)

password = Entry(width=30)
password.grid(column=1, row=3)

password_btn = Button(text="Generate Password", command=generator)
password_btn.grid(column=2, row=3)

add_btn = Button(width=40, text="Add", command=save_info)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
