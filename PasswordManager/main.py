from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for char in range(randint(8, 10))] \
                    + [choice(symbols) for char in range(randint(2, 4))] \
                    + [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    website = website_entry.get()
    email = login_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email, 'password': password
        }
    }


    err_message = ""
    if website == "":
        err_message += "\nEnter the website please!"
    if email == "":
        err_message += "\nEnter the login please!"
    if password == "":
        err_message += "\nEnter the password please!"

    if err_message != "":
        messagebox.showerror(title="Oops", message=err_message)
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} "
                                               f"\nPassword: {password} \nIs it OK to save?")

        if is_ok:
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title=website, message="No Data File Found!")
    else:
        if website in data:
            messagebox.showinfo(title=website,
                                message=f"email: {data[website]['email']} \npassword: {data[website]['password']}")
        else:
            messagebox.showerror(title=website, message="No details for the website exists!")

    # finally:
    #     website_entry.delete(0, END)
    #     password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky=E)

login_label = Label(text="Email/Username: ")
login_label.grid(row=2, column=0, sticky=E)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky=E)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky=E+W)
website_entry.focus()

login_entry = Entry(width=35)
login_entry.insert(0, "angela@gmail.com")
login_entry.grid(row=2, column=1, columnspan=2, sticky=E+W)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=E+W)

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky=E+W)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky=E+W)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=E+W)
# entry1 = Entry(width=36)
# entry1.grid(row=4, column=1, columnspan=2)

# login_entry = Entry(width=35)
# login_entry.pack()
# entry1 = Button(text="Add",width=35)
# entry1.pack()

window.mainloop()