from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
from mysql import connector

# ---------------------------- SEARCH INFO ------------------------------- #
def database():
    try:
        mydb = connector.connect(host="localhost",user="root",password="Hdfc12345@",database="PasswordManager",auth_plugin='mysql_native_password')
        return mydb
    except:
        messagebox.showinfo(title="Error", message=("Database connection failed, Please check and try again"))
        
def search():

    try:
        mydb = database()
        cursor = mydb.cursor(dictionary=True)
        websiteToSearch = website_text.get()
        cursor.execute(f'''SELECT WebsiteName,Email,Password from Data where WebsiteName = "{websiteToSearch}";''')
        result = cursor.fetchone()
        mydb.commit()
        mydb.close()
        print(result)
        messagebox.showinfo(title=websiteToSearch, message=f"Email:{result.get('Email')}\nPassword:{result.get('Password')}")
        # website_text.delete(0,END)
    except:
        messagebox.showinfo(title="Error", message="Something went wrong while fetching data !")
        

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
        try:
            mydb = database()
            cursor = mydb.cursor(dictionary=True)
            cursor.execute(f'''INSERT INTO PasswordManager.Data (WebsiteName,Email,Password) VALUES ("{website}","{username}","{password}");''')
            mydb.commit()
            mydb.close()
            messagebox.showinfo(title="Sucessful", message="Username and Password added sucessfully !!")
        except:
            messagebox.showinfo(title="Error", message="Something went wrong !")
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