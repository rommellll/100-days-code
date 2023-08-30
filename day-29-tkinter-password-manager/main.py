from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

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
    website = website_input.get()
    password = password_input.get()

    if len(email) ==0 or len(website) ==0 or len(password) == 0:
        messagebox.showinfo(title="Oooops!", message="Please make sure you did not leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password}"
                                                     f"\nIs it ok to save?")
        if is_ok:
            with open("saved_password.txt","a") as data:
                data.write(f"{website} | {email} | {password}\n")
            password_input.delete(0, END)
            website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

# Row 1 label and input
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

# Row 2
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

# Row 3
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate", width=10, command=generate_password)
generate_button.grid(column=2, row=3)

# Row 4
add_button = Button(text="Add", width=32, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
