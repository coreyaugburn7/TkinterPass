from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    password_symbols = [password_list.append(random.choice(symbols)) for c in range(nr_symbols)]

    password_numbers = [password_list.append(random.choice(numbers)) for ch in range(nr_numbers)]

    #for char in range(nr_letters):
        #password_list.append(random.choice(letters))

    #for char in range(nr_symbols):
        #password_list += random.choice(symbols)

    #for char in range(nr_numbers):
        #password_list += random.choice(numbers)


    #password_letters = [random.choice(letters) for _ in range(nr_letters)]

    #password_symbols = [choice(letters) for _ in range(randint(8, 10))]

    #password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    #same
    #password = ""
    #for char in password_list:
        #password += char

    print(f"Your password is: {password}")

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return canvas

    is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details you entered. "
                                                                      f"\nEmail: {email_entry.get()} "
                                                                      f"\nPassword: {password_entry.get()} "
                                                                      f"\nIs it ok to save?")


    if is_ok:
        with open("data.txt", mode="a") as data:
            data.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "coreyaugburn7@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()





