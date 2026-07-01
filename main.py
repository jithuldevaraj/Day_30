import tkinter
from tkinter import messagebox
import random



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(event=None):
    # 1. Get the data
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Field empty check
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please enter all required information")

    else:
        # Pop-Up Message
        is_ok = messagebox.askokcancel(title=website, message=f"\nEmail: {email}"
                                                              f"\nPassword: {password} \n\nis it ok to save ?")
        if is_ok:
            # 2.Open the file in append mode and write the data
            with open("./data.txt", mode="a") as data_file:
                data_file.write(f"{website}  |  {email}  |  {password}\n")

            # 3.Clear the website and password entries
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

            # 4.Put the cursor back in website entry
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, bg="white")
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)

#  labels and Entries
website_label = tkinter.Label(text="Website : ")
website_label.grid(row=1, column=0, sticky="E") # Aligns label to the right (East)
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW") # Stretches to fill space
website_entry.focus()

email_label = tkinter.Label(text="Email/Username : ")
email_label.grid(row=2, column=0, sticky="E")
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "studynumber0001@gmail.com")

password_label= tkinter.Label(text= "Password : ")
password_label.grid(row=3, column=0, sticky="E")
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW") # Stretches to match the layout

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
window.bind("<Return>", save)  # Listen for the Keyboard "ENTER" key



window.mainloop()
