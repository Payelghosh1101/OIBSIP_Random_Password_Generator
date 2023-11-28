from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

root = Tk()
root.title("Random Password Generator App")
root.geometry("600x900")
root.configure(bg="#adad85")


def generate_password(length, uppercase = True, lowercase = True, digit = True, punctuation = True ):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digit:
        characters += string.digits
    if punctuation:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Invalid! Please select atleast 1 character")
        return None
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def generate_password_and_update():
    password_length = int(length_var.get())
    uppercase = uppercase_var.get() == "checked"
    lowercase = lowercase_var.get() ==  "checked"
    digit = digit_var.get() ==  "checked"
    punctuation = punctuation_var.get() ==  "checked"

    generated_password = generate_password(password_length, uppercase, lowercase, digit, punctuation)

    if generated_password:
        passwordField.insert(0, generated_password)

def copy_to_clipboard():
    generated_password = passwordField.get()
    pyperclip.copy(generated_password)
    messagebox.showinfo("Success", "Password copied to clipboard!")

f = ("poppins", 25, "bold")
t = ("poppins", 15, "bold")



length_label = Label(root, text="Password Length: ", font=t, background="#adad85")
length_label.pack(padx=10,pady=10)

length_var = IntVar()
length_entry = Entry(root, textvariable=length_var, width=20, font=t, bd = 25,background="#adad85",)
length_entry.pack(padx=10,pady=10)
length_var.set(0)

uppercase_var = StringVar()
uppercase_check = Checkbutton(root, text="Uppercase", font=t,background="#adad85",onvalue="checked", offvalue="", variable=uppercase_var)
uppercase_check.pack(padx=10,pady=10)


lowercase_var = StringVar()
lowercase_check = Checkbutton(root, text="Lowercase", font=t,background="#adad85",onvalue="checked", offvalue="", variable=lowercase_var)
lowercase_check.pack(padx=10,pady=10)


digit_var = StringVar()
digit_check = Checkbutton(root, text="Digits", font=t,background="#adad85",onvalue="checked", offvalue="", variable=digit_var)
digit_check.pack(padx=10,pady=10)


punctuation_var = StringVar()
punctuation_check = Checkbutton(root, text="Symbols", font=t,background="#adad85",onvalue="checked", offvalue="", variable=punctuation_var)
punctuation_check.pack(padx=10,pady=10)


generate_button = Button(root, text="Generate Password",background="#00e600", font=t,command=generate_password_and_update)
generate_button.pack(padx=10, pady=10)

passwordField = Entry(root, width=25,background="#adad85", bd=20, font=f)
passwordField.pack(pady=10)

copy_button = Button(root, text="Copy to Clipboard",background="#ccccb3", font=t,command=copy_to_clipboard)
copy_button.pack(padx=10, pady=10)

exit_button = Button(root, text="EXIT",font=t, background='red', command=lambda:root.destroy())
exit_button.pack(padx=10,pady=10)
root.mainloop()