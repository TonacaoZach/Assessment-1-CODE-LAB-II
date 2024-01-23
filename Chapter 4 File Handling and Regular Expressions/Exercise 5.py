import tkinter as tk
from tkinter import messagebox

class PasswordValidatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Validator")

        # Variables
        self.attempts_remaining = 5

        # Widgets

        self.label = tk.Label(master, text="Contain at least 1 letter between a and z \nContain at least 1 number between 0 and 9 \nContain at least 1 letter between A and Z\nContain at least 1 character from $, #, @\nMinimum length of password: 6\nMaximum length of password: 12")
        self.label.pack(pady=10)
        
        self.label = tk.Label(master, text="Enter Password:")
        self.label.pack(pady=10)

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.validate_password)
        self.submit_button.pack(pady=10)

    def validate_password(self):
        password = self.password_entry.get()
        if self.is_valid_password(password):
            messagebox.showinfo("Success", "Password is valid!")
            self.master.destroy()
        else:
            self.attempts_remaining -= 1
            if self.attempts_remaining > 0:
                messagebox.showwarning("Invalid Password", f"Invalid password! {self.attempts_remaining} attempts remaining.")
            else:
                messagebox.showerror("Alert", "Authorities have been alerted! Too many failed attempts.")
                self.master.destroy()

    def is_valid_password(self, password):
        return (
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            any(char.isupper() for char in password) and
            any(char in "$#@ " for char in password) and
            6 <= len(password) <= 12
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordValidatorApp(root)
    root.mainloop()
