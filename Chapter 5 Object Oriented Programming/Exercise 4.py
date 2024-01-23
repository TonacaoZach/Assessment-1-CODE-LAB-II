import tkinter as tk
from tkinter import messagebox
import math

class Shape:
    def __init__(self):
        self.sides = []

    def input_sides(self):
        pass

    def area(self):
        pass

class Circle(Shape):
    def input_sides(self):
        radius = float(entry_radius.get())
        self.sides = [radius]

    def area(self):
        return math.pi * self.sides[0] ** 2

class Rectangle(Shape):
    def input_sides(self):
        length = float(entry_length.get())
        width = float(entry_width.get())
        self.sides = [length, width]

    def area(self):
        return self.sides[0] * self.sides[1]

class Triangle(Shape):
    def input_sides(self):
        side_a = float(entry_side_a.get())
        side_b = float(entry_side_b.get())
        side_c = float(entry_side_c.get())
        self.sides = [side_a, side_b, side_c]

    def area(self):
        s = sum(self.sides) / 2
        return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))

def calculate_area():
    selected_shape = shape_var.get()
    shape_dict[selected_shape].input_sides()
    try:
        area_result.set(f"Area: {shape_dict[selected_shape].area():.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for sides.")

def show_entries(selected_shape):
    label_radius.pack_forget()
    entry_radius.pack_forget()
    label_length.pack_forget()
    entry_length.pack_forget()
    label_width.pack_forget()
    entry_width.pack_forget()
    label_side_a.pack_forget()
    entry_side_a.pack_forget()
    label_side_b.pack_forget()
    entry_side_b.pack_forget()
    label_side_c.pack_forget()
    entry_side_c.pack_forget()

    if selected_shape == "Circle":
        label_radius.pack(pady=5)
        entry_radius.pack(pady=5)
    elif selected_shape == "Rectangle":
        label_length.pack(pady=5)
        entry_length.pack(pady=5)
        label_width.pack(pady=5)
        entry_width.pack(pady=5)
    elif selected_shape == "Triangle":
        label_side_a.pack(pady=5)
        entry_side_a.pack(pady=5)
        label_side_b.pack(pady=5)
        entry_side_b.pack(pady=5)
        label_side_c.pack(pady=5)
        entry_side_c.pack(pady=5)

# Create the main window
root = tk.Tk()
root.title("Shape Area Calculator")

# Create and set up widgets
shape_label = tk.Label(root, text="Select Shape:")
shape_label.pack(pady=10)

shape_var = tk.StringVar()
shape_var.set("Circle")

shape_menu = tk.OptionMenu(root, shape_var, "Circle", "Rectangle", "Triangle")
shape_menu.pack(pady=10)

label_radius = tk.Label(root, text="Enter Radius:")
label_length = tk.Label(root, text="Enter Length:")
label_width = tk.Label(root, text="Enter Width:")
label_side_a = tk.Label(root, text="Enter Side A:")
label_side_b = tk.Label(root, text="Enter Side B:")
label_side_c = tk.Label(root, text="Enter Side C:")

entry_radius = tk.Entry(root)
entry_length = tk.Entry(root)
entry_width = tk.Entry(root)
entry_side_a = tk.Entry(root)
entry_side_b = tk.Entry(root)
entry_side_c = tk.Entry(root)

shape_var.trace_add("write", lambda *args: show_entries(shape_var.get()))

calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.pack(pady=10)

area_result = tk.StringVar()
area_result_label = tk.Label(root, textvariable=area_result)
area_result_label.pack(pady=10)

# Create instances of the shape classes
circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

# Store shape instances in a dictionary for easy access
shape_dict = {"Circle": circle, "Rectangle": rectangle, "Triangle": triangle}

# Run the Tkinter event loop
root.mainloop()
