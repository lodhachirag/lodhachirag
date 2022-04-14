from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

# ---------------------------- SEARCH INFO ------------------------------- #


def search():
    global website
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=("File not found plz check again!"))
    else:
        try:
            website = website_text.get()
            website_info = data.get(website)
            email_info = website_info.get("email")
            password_info = website_info.get("password")
            messagebox.showinfo(title=website, message=f"Email:{email_info}\nPassword:{password_info}")
            website_text.delete(0,END)
        except AttributeError:
            messagebox.showinfo(title="Error", message=f"You dont save {website} username and password in password manager")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    Password_text.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for i in range(randint(3,4))]
    password_number = [choice(numbers) for i in range(randint(2,4))]
    password_symbol = [choice(symbols) for i in range(randint(3,4))]

    password_list = password_letter + password_number + password_symbol
    shuffle(password_list)
    password = "".join(password_list)

    Password_text.insert(0, password)
    # pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website = website_text.get()
    username = Username_text.get()
    password = Password_text.get()
    if len(website) == 0 or len(password)==0:
        messagebox.showinfo(title="Error", message="Dont left any field blank!")
    else:
        new_data = {
            website: {
                "email":username,
                "password":password
            }
        }
        try:
            with open("Python/GUIPAsswordManager/data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("Python/GUIPAsswordManager/data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("Python/GUIPAsswordManager/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        website_text.delete(0, END)
        Password_text.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="Python/GUIPAsswordManager/logo.png")
canvas.create_image(100, 100, image=image, anchor="center")
canvas.grid(row=0, column=1, pady=20)

#Lables
website_label = Label(text="Website:", font=("", 14, "bold"))
website_label.grid(row=1, column=0)

Username_label = Label(text="Email/Username:", font=("", 14, "bold"))
Username_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("", 14, "bold"))
password_label.grid(row=3, column=0)

#Entry
website_text = Entry(width=30)
website_text.grid(row=1,column=1)
website_text.focus()

Username_text = Entry(width=54)
Username_text.grid(row=2,column=1, columnspan=2)
Username_text.insert(0, "chiraglodha999@gmail.com")

Password_text = Entry(width=54)
Password_text.grid(row=3, column=1, columnspan =2)

#Button
Generate_button = Button(text="Generate Password",highlightthickness=0, command=generate, width =16)
Generate_button.grid(row=4, column=2, padx= 12)

Add_button = Button(text="Add", highlightthickness=0, width=25 , command=add)
Add_button.grid(row=4, column=1, pady=10)

Search_button = Button(text = "Search",highlightthickness=0, width= 16, command=search)
Search_button.grid(row =1, column=2)

window.mainloop()