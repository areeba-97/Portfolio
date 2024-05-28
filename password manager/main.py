from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def delete_entry():
    # Delete the Entries
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill out all the empty fields")

    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"You entered following details:\n\n"
        #                                                       f"Email:{email}\n Password:{password}.\n\n"
        #                                                       f"Ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as text_file:
                # Reading old data
                data = json.load(text_file)
                # Updating old data with new data
                data.update(new_data)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as text_file:
                # Creating new file
                json.dump(new_data, text_file, indent=4)

        else:
            with open("data.json", "w") as text_file:
                # Saving updated data
                json.dump(data, text_file, indent=4)

            # text_file.write(f" {website} | {email} | {password}\n")

        finally:
            messagebox.showinfo(title=website, message=f"{website} information has been saved.")
            delete_entry()


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as text_file:
            details = json.load(text_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if website in details:
            email = details[website]['email']
            password = details[website]['password']
            messagebox.showinfo(title=website, message="Following are the details: \n\n"
                                                       f"Email:{email}\n Password:{password}.")
        else:
            messagebox.showinfo(title="Error", message=f"No details of {website} exits.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
# Canvas
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
# Labels
website_name = Label(text="Website:")
website_name.grid(row=1, column=0)
website_name.focus()

email_name = Label(text="Email/Username:")
email_name.grid(row=2, column=0)

password_name = Label(text="Password:")
password_name.grid(row=3, column=0)
# Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, sticky="EW")

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "areeba.altaf@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky="W")
# Buttons
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2, sticky="EW")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", )

window.mainloop()
