import tkinter as tk
from tkinter import filedialog, messagebox

class CharacterOccurrenceCounter:
    def __init__(self, master):
        self.master = master
        master.title("Character Occurrence Counter")

        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.master, text="Enter a character:")
        self.instruction_label.pack(pady=10)

        self.entry = tk.Entry(self.master, width=5)
        self.entry.pack(pady=10)

        self.browse_button = tk.Button(self.master, text="Browse File", command=self.browse_file)
        self.browse_button.pack(pady=10)

        self.count_button = tk.Button(self.master, text="Count Occurrences", command=self.get_user_input)
        self.count_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.file_path = file_path
            messagebox.showinfo("File Selected", f"Selected file: {file_path}")
        else:
            messagebox.showwarning("No File Selected", "Please select a valid text file.")

    def count_occurrences(self, character):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            count = content.count(character)
            return count
        except FileNotFoundError:
            return None

    def get_user_input(self):
        if not hasattr(self, 'file_path'):
            messagebox.showwarning("No File Selected", "Please select a valid text file.")
            return

        character = self.entry.get().lower()
        if len(character) == 1 and character.isalpha():
            occurrences = self.count_occurrences(character)
            if occurrences is not None:
                self.result_label.config(text=f"Occurrences of '{character}': {occurrences}")
            else:
                self.result_label.config(text="File not found or empty.")
        else:
            messagebox.showerror("Error", "Please enter a single alphabetical character.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterOccurrenceCounter(root)
    root.mainloop()
