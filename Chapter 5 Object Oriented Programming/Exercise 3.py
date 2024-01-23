from tkinter import messagebox, Tk, Label, Entry, Button, Text, END


class Employee:
    def __init__(self, name="", position="", salary=0.0, emp_id=0):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id

    def set_data(self, name, position, salary, emp_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id

    def get_data(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"


class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Data Entry")

        self.employees = []

        # Initialize entries as an instance variable
        self.entries = []

        self.create_widgets()

    def create_widgets(self):
        labels = ["Name", "Position", "Salary", "ID"]

        for row, label_text in enumerate(labels):
            Label(self.master, text=f"{label_text}:").grid(row=row, column=0, pady=5)
            entry = Entry(self.master)
            self.entries.append(entry)
            entry.grid(row=row, column=1, padx=10, pady=5)

        Button(self.master, text="Add Employee", command=self.add_employee).grid(row=row + 1, column=0, columnspan=2, pady=10)
        Button(self.master, text="Display Employees", command=self.display_employees).grid(row=row + 2, column=0, columnspan=2)

        self.text_output = Text(self.master, height=10, width=50)
        self.text_output.grid(row=row + 3, column=0, columnspan=2, pady=10)

    def add_employee(self):
        data = [entry.get() for entry in self.entries[1:]]  # Use self.entries to fix the NameError
        try:
            salary, emp_id = map(float, data[1:3])
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for Salary and ID.")
            return

        employee = Employee(name=self.entries[0].get(), position=data[0], salary=salary, emp_id=emp_id)
        self.employees.append(employee)

        # Clear the entry fields
        for entry in self.entries:
            entry.delete(0, END)

        messagebox.showinfo("Success", "Employee added successfully!")

    def display_employees(self):
        output_text = "Name\tPosition\tSalary\tID\n"
        output_text += "--------------------------------\n"
        for employee in self.employees:
            output_text += employee.get_data() + "\n"

        self.text_output.delete(1.0, END)  # Clear previous content
        self.text_output.insert(END, output_text)


if __name__ == "__main__":
    root = Tk()
    app = EmployeeGUI(root)
    root.mainloop()
