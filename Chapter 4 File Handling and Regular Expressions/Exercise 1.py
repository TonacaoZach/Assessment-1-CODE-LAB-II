import tkinter as tk
from tkinter import *
from customtkinter import *
import os

root = tk.Tk()
root.geometry("340x300")
root.resizable(width=False, height=False)
root.title("BathSpa University")

def submit():
    Sname1 = Sname.get()
    Age1 = int(Age.get())
    HAdd1 = HAdd.get()
    print("Name:", Sname1)
    print("Age:", Age1)
    print("Home Address:", HAdd1)

    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "ex1.txt")

    with open(file_path, "w") as file:
        file.write(f"{Sname1}\n{Age1}\n{HAdd1}\n")
    print(f"Username: {Sname1}\nAge: {Age1}\nHometown: {HAdd1}\n")

Sname_label = Label(root, text="Username") 

Age_label = Label(root, text="Age")

HAdd_label = Label(root, text="Home Address")

Sname_label.place(x=20, y=60)

Age_label.place(x=20, y=90)

HAdd_label.place(x=20, y=120)

Sname = CTkEntry(root, font=("Helvetica", 12), corner_radius=0, border_color="#adaeb7", height=25, width=161.45, fg_color="#adaeb7")
Sname.place(x=148.3, y=60)

Age = CTkEntry(root, font=("Helvetica", 12), corner_radius=0, border_color="#adaeb7", height=25, width=161.45, fg_color="#adaeb7")
Age.place(x=148.3, y=90)

HAdd = CTkEntry(root, font=("Helvetica", 12), corner_radius=0, border_color="#adaeb7", height=25, width=161.45, fg_color="#adaeb7")
HAdd.place(x=147, y=120)

button = CTkButton(root, text="Submit", font=("Helvetica", 13), fg_color="#22263d", corner_radius=0, text_color="White",
                   border_width=0, height=38, width=112, command=submit)
button.place(x=35.6, y=150)

root.mainloop()
