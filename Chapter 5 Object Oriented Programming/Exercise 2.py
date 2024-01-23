import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        average = (self.mark1 + self.mark2 + self.mark3) / 3
        return average

    def display(self):
        average = self.calcGrade()
        messagebox.showinfo("Student Information", f"Name: {self.name}\nAverage Grade: {average:.2f}")

class StudentsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Students GUI")

        # Create the first student object
        self.student1 = Students("John Doe", 80, 90, 75)

        # Create Labels for user input
        tk.Label(master, text="Enter Name:").pack(pady=5)
        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.pack(pady=5)

        tk.Label(master, text="Enter Mark 1:").pack(pady=5)
        self.mark1_entry = tk.Entry(master, width=30)
        self.mark1_entry.pack(pady=5)

        tk.Label(master, text="Enter Mark 2:").pack(pady=5)
        self.mark2_entry = tk.Entry(master, width=30)
        self.mark2_entry.pack(pady=5)

        tk.Label(master, text="Enter Mark 3:").pack(pady=5)
        self.mark3_entry = tk.Entry(master, width=30)
        self.mark3_entry.pack(pady=5)

        # Create Button to display student information
        self.display_button = tk.Button(master, text="Display Student Info", command=self.display_info)
        self.display_button.pack(pady=10)

    def display_info(self):
        try:
            # Get user input values
            name = self.name_entry.get()
            mark1 = int(self.mark1_entry.get())
            mark2 = int(self.mark2_entry.get())
            mark3 = int(self.mark3_entry.get())

            # Create the second student object with user input values
            student2 = Students(name, mark1, mark2, mark3)
            student2.display()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for marks.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentsGUI(root)
    root.mainloop()
