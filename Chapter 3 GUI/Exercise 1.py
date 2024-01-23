from tkinter import *

def update_message():
    user_name = name_entry.get()
    selected_color = color_var.get()
    greeting_label.config(text=f"Hello, {user_name}!", fg=selected_color)

# Main Window
app_window = Tk()

# Input Frame
input_frame = Frame(app_window, bg="#a0c8ff")
input_frame.pack(padx=10, pady=10)

input_title = Label(input_frame, text="User Input", bg="#a0c8ff", fg="black", font=("Arial", 15, "bold"), padx=10, pady=10)
input_title.pack()

name_label = Label(input_frame, text="Enter your name: ", bg="#a0c8ff", fg="black", font=("Arial", 10, "bold"), padx=10, pady=10)
name_label.pack()

name_entry = Entry(input_frame)
name_entry.pack()

color_label = Label(input_frame, text="Choose a color: ", bg="#a0c8ff", fg="black", font=("Arial", 10, "bold"), padx=15, pady=5)
color_label.pack()

available_colors = ["red", "yellow", "blue", "lightgreen", "pink"]
color_var = StringVar()
color_dropdown = OptionMenu(input_frame, color_var, *available_colors)
color_dropdown.configure(border=0)
color_var.set("red")  # sets the default color
color_dropdown.pack(pady=10)

update_button = Button(input_frame, text="Update Greeting", command=update_message)
update_button.pack(pady=10)

# Display Frame
display_frame = Frame(app_window)
display_frame.pack(padx=10, pady=10)

display_title = Label(display_frame, text="Display Greeting", bg="#a0ffd4", font=("Arial", 10, "bold"), fg="black", padx=10, pady=10)
display_title.pack()

greeting_label = Label(display_frame, text=" ", bg="#a0ffd4", fg="black", font=("Arial", 10, "bold"), padx=25)
greeting_label.pack()

app_window.mainloop()
