import random
import pyperclip
from tkinter import *
from tkinter import messagebox

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!',
              '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pwd_complexity():
    return int(var.get())

def pwd_generator():
    pwd_length = pwd_complexity()
    pwd_list = []

    for char in range(pwd_length):
        pwd_list.append(random.choice(characters))

    pwd = "".join(pwd_list)
    entry_pwd.insert(0,pwd)
    pyperclip.copy(pwd)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_text():
    website = entry_website.get()
    username = entry_email_username.get()
    pwd = entry_pwd.get()
    txt_to_append = f"{website} | {username} | {pwd}\n"

    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title = "Ooops", message = "Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title = f"Confirmation - {website}", message = f"These are the details "
                                                                                    f"entered:\nEmail: {username} \nPassword: {pwd}\n\n Is it ok to save?")

        if is_ok:
            with open('data.txt','a') as f:
                f.writelines(txt_to_append)
                entry_pwd.delete(0, END)
                entry_website.delete(0, END)
                var.set(3)
        else:
            entry_pwd.delete(0, END)
            entry_website.delete(0, END)

    entry_website.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img,)
canvas.grid(column = 1,row = 0)

#Labels
lbl_website = Label()
lbl_website.config(text = "Website:")
lbl_website.grid(column = 0, row = 1,pady = 3)

lbl_email_username = Label()
lbl_email_username.config(text = "Email/Username:")
lbl_email_username.grid(column = 0, row = 2,pady = 3)

lbl_pwd = Label()
lbl_pwd.config(text = "Password:")
lbl_pwd.grid(column = 0, row = 6,pady = 3)

lbl_pwd_length = Label()
lbl_pwd_length.config(text = "Password length:")
lbl_pwd_length.grid(column = 0, row = 3,pady = 3)

#Entry
entry_website = Entry(width = 50)
entry_website.grid(column = 1, row = 1, columnspan = 2)
entry_website.focus()

entry_email_username = Entry(width = 50)
entry_email_username.insert(0, "emailaddress@domain.com")
entry_email_username.grid(column = 1, row = 2, columnspan = 2)

entry_pwd = Entry(width = 32)
entry_pwd.grid(column = 1, row = 6,columnspan = 1)

btn_generate_pwd = Button(command = pwd_generator)
btn_generate_pwd.config(text = "Generate password")
btn_generate_pwd.grid(column = 2,row = 6,padx = 0)

var = IntVar()
R1 = Radiobutton(window, text="30", variable=var, value=30, command=pwd_complexity)
R1.grid( column = 1, row = 3 )
R2 = Radiobutton(window, text="40", variable=var, value=40, command=pwd_complexity)
R2.grid( column = 1, row = 4 )
R3 = Radiobutton(window, text="50", variable=var, value=50, command=pwd_complexity)
R3.grid( column = 1, row = 5 )

btn_add = Button(width = 42,command = save_to_text)
btn_add.config(text = "Add")
btn_add.grid(column = 1,row = 7,columnspan = 2,pady = 3)




window.mainloop()