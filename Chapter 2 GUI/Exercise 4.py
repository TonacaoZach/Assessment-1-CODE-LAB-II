import tkinter as tk
from tkinter import *
from customtkinter import *
from PIL import *

root = tk.Tk()
root.geometry("340x595")
root.resizable(width=False, height=False)
root.title("BathSpa University")

# Function to submit data
def submit():
    Sname1 = Sname.get()
    Mnum1 = Mnum.get()
    Email1 = Email.get()
    HAdd1 = HAdd.get()
    selected_gender = selected_course1.get()
    selected_course_value = selected_course.get()
    english_checked = language.get()
    hindi_urdu_checked = language3.get()
    tagalog_checked = language2.get()
    communication_skill = coms_scale.get()

    # Now you can use the retrieved values as needed 
    print("Student Name:", Sname1)
    print("Mobile Number:", Mnum1)
    print("Email:", Email1)
    print("Home Address:", HAdd1)
    print("Selected Gender:", selected_gender)
    print("Selected Course:", selected_course_value)
    print("\nIf Value is 1 it means CHECKED")
    print("English Checker:", english_checked)
    print("Tagalog Checker:", tagalog_checked)
    print("Hindu Checker:", hindi_urdu_checked)
    print("Communication Skill Level:", communication_skill)

# Background image

canvas1 = tk.Canvas(root, width=750, height=550)
canvas1.pack(fill="both", expand=True)

canvas1.create_image(0, 0, image=bg, anchor="nw")

# Entry
Sname = CTkEntry(root, font=("Helvetica", 12), corner_radius=0, border_color="#adaeb7", height=25, width=161.45, fg_color="#adaeb7")
Sname.place(x=148.3, y=160)

Mnum = CTkEntry(root, font=("Helvetica", 12), corner_radius=0, border_color="#adaeb7", height=25, width=161.45, fg_color="#adaeb7")
Mnum.place(x=148.3, y=197)

Email = CTkEntry(root, font=("Helvetica", 12), corner_radius=0, border_color="#adaeb7", height=25, width=161.45, fg_color="#adaeb7")
Email.place(x=146, y=232)

HAdd = CTkEntry(root, font=("Helvetica", 12), corner_radius=0, border_color="#adaeb7", height=25, width=161.45, fg_color="#adaeb7")
HAdd.place(x=147, y=265)

# Drop Down
selected_course1 = StringVar()
selected_course1.set("")

gender = ['Male', 'Female', 'Prefer Not to Say', 'Other']
dropdown = CTkComboBox(root, values=gender, font=("Helvetica", 12), corner_radius=0, border_color="#adaeb7",
                        height=26, width=161.45, fg_color="#adaeb7", variable=selected_course1,state='readonly')
dropdown.place(x=147, y=300)

# Radio Button
selected_course = StringVar()
selected_course.set(None)

BsCC = Radiobutton(root, text="BSc CC", value="BSc CC", font=("Helvetica", 8), bg="#f5f5f6", variable=selected_course)
BsCC.place(x=160, y=330)

BsCY = Radiobutton(root, text="BSc CY", value="BSc CY", font=("Helvetica", 8), bg="#f5f5f6", variable=selected_course)
BsCY.place(x=160, y=350)

BsPsy = Radiobutton(root, text="BSc Psy", value="BSc Psy", font=("Helvetica", 8), bg="#f5f5f6", variable=selected_course)
BsPsy.place(x=160, y=370)

BaBm = Radiobutton(root, text="BA & BM", value="BA & BM", font=("Helvetica", 8), bg="#f5f5f6", variable=selected_course)
BaBm.place(x=160, y=390)

# Check Boxes
language = IntVar()
language2 = IntVar()
language3 = IntVar()


eng = Checkbutton(root, text="English", font=("Helvetica", 9), bg="#f5f5f6", variable=language)
eng.place(x=150, y=416)

tagalog = Checkbutton(root, text="Tagalog", font=("Helvetica", 9), bg="#f5f5f6", variable=language2)
tagalog.place(x=220, y=416)

hindi_urdu = Checkbutton(root, text="Hindu/Urdu", font=("Helvetica", 9), bg="#f5f5f6", variable=language3)
hindi_urdu.place(x=150, y=440)

# Slide Bar
coms_scale = Scale(root, from_=0, to=10, orient="horizontal", length=200, bg="#f5f5f6", highlightthickness=0)
coms_scale.place(x=70, y=486)

# Button
button = CTkButton(root, text="Submit", font=("Helvetica", 13), fg_color="#22263d", corner_radius=0, text_color="White",
                   border_width=0, height=38, width=112, command=submit)
button.place(x=35.6, y=535)

# Clear function for the Clear button
def cleared():
    Sname.delete(0, tk.END)
    Mnum.delete(0, tk.END)
    Email.delete(0, tk.END)
    HAdd.delete(0, tk.END)
    dropdown.set("")  # Clear the dropdown selection
    BsCC.deselect()   # Deselect radio buttons
    BsCY.deselect()
    BsPsy.deselect()
    BaBm.deselect()
    language.set(0)   # Uncheck checkboxes
    coms_scale.set(0)  # Reset the scale bar

button = CTkButton(root, text="Clear", font=("Helvetica", 13), fg_color="#22263d", corner_radius=0, text_color="White",
                   border_width=0, height=38, width=112, command=cleared)
button.place(x=193, y=534)

root.mainloop()
