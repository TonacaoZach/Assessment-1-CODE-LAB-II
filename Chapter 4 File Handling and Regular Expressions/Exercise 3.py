import tkinter as tk
from tkinter import filedialog

class NumbersViewerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Numbers Viewer")
        
        self.result_text = tk.StringVar()
        self.result_label = tk.Label(self.master, textvariable=self.result_text, justify=tk.LEFT)
        self.result_label.pack(padx=10, pady=10)

        self.open_file_button = tk.Button(self.master, text="Open File", command=self.open_file_dialog)
        self.open_file_button.pack(pady=10)

    def read_numbers_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                numbers = [int(line.strip()) for line in file]
            return numbers
        except FileNotFoundError:
            return None

    def show_numbers(self, file_path):
        numbers = self.read_numbers_from_file(file_path)
        if numbers is not None:
            self.result_text.set("\n".join(map(str, numbers)))
        else:
            self.result_text.set(f"File not found: {file_path}")

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.show_numbers(file_path)

def main():
    root = tk.Tk()
    app = NumbersViewerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
