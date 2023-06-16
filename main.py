import tkinter as gui
from tkinter import messagebox
import random as r
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [r.choice(letters) for _ in range(r.randint(8, 10))]
    pw_symbols = [r.choice(symbols) for _ in range(r.randint(2, 4))]
    pw_numbers = [r.choice(numbers) for _ in range(r.randint(2, 4))]
    password_list = pw_letters + pw_symbols + pw_numbers
    r.shuffle(password_list)
    password = "".join(password_list)
    pw_input.delete(0, "end")
    pw_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    email = email_input.get()
    pw = pw_input.get()
    website = website_input.get()

    if len(email) == 0 or len(pw) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                              f"Password: {pw}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {pw}\n")
            website_input.delete(0, "end")
            pw_input.delete(0, "end")


# ---------------------------- UI ------------------------------- #
window = gui.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = gui.PhotoImage(file="logo.png")

canvas = gui.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = gui.Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = gui.Entry(width=53)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = gui.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = gui.Entry(width=53)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "EMAIL@HERE.COM")

pw_label = gui.Label(text="Password:")
pw_label.grid(column=0, row=3)

pw_input = gui.Entry(width=35)
pw_input.grid(column=1, row=3)

pw_generate_button = gui.Button(text="Generate Password", command=gen_pw)
pw_generate_button.grid(column=2, row=3)

add_button = gui.Button(text="Add", width=45, command=save_pw)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
