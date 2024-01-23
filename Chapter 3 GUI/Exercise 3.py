import tkinter as tk
from tkinter import ttk

class AreaCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Area Function")
        self.geometry("300x200")
        
        self.create_tabs()
    
    def create_tabs(self):
        notebook = ttk.Notebook(self)
        notebook.pack(pady=15)

        CircleFrame(notebook, text="Circle")
        SquareFrame(notebook, text="Square")
        RectangleFrame(notebook, text="Rectangle")

class ShapeFrame(ttk.Frame):
    def __init__(self, notebook, text):
        super().__init__(notebook)
        notebook.add(self, text=text)
        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self, text=self.title_text(), font=("Arial", 15, "bold"))
        title_label.grid(column=1, row=0)

        self.create_input_widgets()
        self.create_result_widgets()

    def create_input_widgets(self):
        pass

    def create_result_widgets(self):
        pass

    def title_text(self):
        return f"{self.shape_name()} Area Calculator"

    def shape_name(self):
        raise NotImplementedError("Subclasses must implement shape_name method.")

class CircleFrame(ShapeFrame):
    def create_input_widgets(self):
        radius_label = ttk.Label(self, text="Radius", font=("Arial", 10))
        radius_label.grid(row=1, column=0)

        self.radius_var = tk.IntVar()
        radius_entry = ttk.Entry(self, textvariable=self.radius_var)
        radius_entry.grid(row=1, column=1, pady=5)

        calculate_button = ttk.Button(self, text="Calculate", command=self.display_area)
        calculate_button.grid(row=3, column=1, pady=5)

    def create_result_widgets(self):
        self.area_label = ttk.Label(self, text="", font=("Arial", 10))
        self.area_label.grid(row=2, column=1, columnspan=2)

    def display_area(self):
        area = self.calculate_area()
        self.area_label.config(text=f"The area of the circle is {area}.")

    def calculate_area(self):
        radius_value = self.radius_var.get()
        return radius_value ** 2 * 3.14

    def shape_name(self):
        return "Circle"

class SquareFrame(ShapeFrame):
    def create_input_widgets(self):
        side_label = ttk.Label(self, text="Side", font=("Arial", 10))
        side_label.grid(row=1, column=0)

        self.side_var = tk.IntVar()
        side_entry = ttk.Entry(self, textvariable=self.side_var)
        side_entry.grid(row=1, column=1, pady=5)

        calculate_button = ttk.Button(self, text="Calculate", command=self.display_area)
        calculate_button.grid(row=3, column=1, pady=5)

    def create_result_widgets(self):
        self.area_label = ttk.Label(self, text="", font=("Arial", 10))
        self.area_label.grid(row=2, column=1, columnspan=2)

    def display_area(self):
        area = self.calculate_area()
        self.area_label.config(text=f"The area of the square is {area}.")

    def calculate_area(self):
        side_value = self.side_var.get()
        return side_value ** 2

    def shape_name(self):
        return "Square"

class RectangleFrame(ShapeFrame):
    def create_input_widgets(self):
        width_label = ttk.Label(self, text="Width", font=("Arial", 10))
        width_label.grid(row=1, column=0)

        self.width_var = tk.IntVar()
        width_entry = ttk.Entry(self, textvariable=self.width_var)
        width_entry.grid(row=1, column=1, pady=5)

        length_label = ttk.Label(self, text="Length", font=("Arial", 10))
        length_label.grid(row=2, column=0)

        self.length_var = tk.IntVar()
        length_entry = ttk.Entry(self, textvariable=self.length_var)
        length_entry.grid(row=2, column=1, pady=5)

        calculate_button = ttk.Button(self, text="Calculate", command=self.display_area)
        calculate_button.grid(row=4, column=1, pady=5)

    def create_result_widgets(self):
        self.area_label = ttk.Label(self, text="", font=("Arial", 10))
        self.area_label.grid(row=3, column=1, columnspan=2)

    def display_area(self):
        area = self.calculate_area()
        self.area_label.config(text=f"The area of the rectangle is {area}.")

    def calculate_area(self):
        width_value = self.width_var.get()
        length_value = self.length_var.get()
        return width_value * length_value

    def shape_name(self):
        return "Rectangle"

if __name__ == "__main__":
    app = AreaCalculator()
    app.mainloop()
