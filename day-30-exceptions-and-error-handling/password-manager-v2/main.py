from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""
    password_input.delete(0, END)
    window.clipboard_clear()

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(END, string=password)
    window.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_input.get()
    website = website_input.get().lower()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oooops!", message="Please make sure you did not leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            if website in data:
                existing_email = (data[website]["email"])
                is_ok = messagebox.askokcancel(title="Information!",
                                               message=f"The {website} is already in the data file with the email {existing_email}."
                                                       f" \nPress ok to overwrite.")
                if is_ok:
                    # Updating old data
                    data.update(new_data)
                    with open("data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)
        finally:
            password_input.delete(0, END)
            website_input.delete(0, END)


def find_password():
    website = website_input.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found.")
    else:
        if website in data:
            website_data = data[website]
            email = website_data["email"]
            password = website_data["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Information", message=f"No details found for the website {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=33)
website_input.focus()
website_input.grid(column=1, row=1)

email_input = Entry(width=43)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=7, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
