import tkinter as tk
from tkinter import ttk, messagebox

class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, operation, num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == "Addition":
                self.result = num1 + num2
            elif operation == "Subtraction":
                self.result = num1 - num2
            elif operation == "Multiplication":
                self.result = num1 * num2
            elif operation == "Division":
                if num2 != 0:
                    self.result = num1 / num2
                else:
                    messagebox.showerror("Error", "Division by zero is not allowed.")
                    return None

            return self.result

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")
            return None

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arithmetic Calculator")

        # Create instances of ArithmeticOperations class
        self.arithmetic_operations = ArithmeticOperations()

        # Set styles
        style = ttk.Style()
        style.configure("TLabel", font=('Helvetica', 14))
        style.configure("TButton", font=('Helvetica', 12))

        # Create widgets
        self.label_operation = ttk.Label(master, text="Select Operation:")
        self.label_operation.pack(pady=10)

        self.operation_var = tk.StringVar()
        self.operation_var.set("Addition")

        self.operation_menu = ttk.Combobox(master, textvariable=self.operation_var, values=["Addition", "Subtraction", "Multiplication", "Division"])
        self.operation_menu.pack(pady=10)

        self.label_num1 = ttk.Label(master, text="Enter Number 1:")
        self.label_num1.pack(pady=5)

        self.entry_num1 = ttk.Entry(master)
        self.entry_num1.pack(pady=5)

        self.label_num2 = ttk.Label(master, text="Enter Number 2:")
        self.label_num2.pack(pady=5)

        self.entry_num2 = ttk.Entry(master)
        self.entry_num2.pack(pady=5)

        self.button_calculate = ttk.Button(master, text="Calculate", command=self.calculate_operation)
        self.button_calculate.pack(pady=10)

        self.label_result = ttk.Label(master, text="Result:")
        self.label_result.pack()

    def calculate_operation(self):
        operation = self.operation_var.get()
        num1 = self.entry_num1.get()
        num2 = self.entry_num2.get()

        result = self.arithmetic_operations.calculate(operation, num1, num2)

        if result is not None:
            self.label_result.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.geometry("340x400")
    root.mainloop()
