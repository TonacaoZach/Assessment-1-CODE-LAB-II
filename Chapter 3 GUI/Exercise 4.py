import tkinter as tk
from tkinter import *

class ShapeDrawerApp:
    def __init__(self, master):
        self.master = master
        master.title("Shape Drawer")

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.shape_var = tk.StringVar()
        self.shape_var.set("Oval")

        shape_lbl = tk.Label(master, text="Pick a shape")
        shape_lbl.pack()

        shape_menu = tk.OptionMenu(master, self.shape_var, "Oval", "Rectangle", "Square", "Triangle")
        shape_menu.pack()

        coord_lbl = tk.Label(master, text="Enter your coordinates (Ex. 120 430 200 12):")
        coord_lbl.pack()

        self.coord_entry = tk.Entry(master)
        self.coord_entry.pack()

        draw_btn = tk.Button(master, text="Draw", command=self.draw_shape)
        draw_btn.pack()

    def validate_coords(self, coords, expected_length):
        if len(coords) != expected_length:
            print(f"Error: Invalid number of coordinates. Expected {expected_length}, got {len(coords)}.")
            return False
        try:
            int_coords = list(map(int, coords))
            return int_coords
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def draw_shape(self):
        shape = self.shape_var.get()
        coord = self.coord_entry.get()

        coords = coord.split()

        if shape == "Oval" and self.validate_coords(coords, 4):
            self.canvas.create_oval(coords, fill="lightblue")
        elif shape == "Rectangle" and self.validate_coords(coords, 4):
            self.canvas.create_rectangle(coords, fill="lightblue")
        elif shape == "Square" and self.validate_coords(coords, 4):
            x1, y1, x2, y2 = self.validate_coords(coords, 4)
            side_length = min(x2 - x1, y2 - y1)
            self.canvas.create_rectangle(x1, y1, x1 + side_length, y1 + side_length, fill="lightblue")
        elif shape == "Triangle" and self.validate_coords(coords, 6):
            self.canvas.create_polygon(coords, fill="lightblue")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawerApp(root)
    root.mainloop()
