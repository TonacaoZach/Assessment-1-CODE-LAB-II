from tkinter import *
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    
    if file_path:
        file_entry.config(state="normal")
        file_entry.delete(0, END)
        file_entry.insert(0, file_path)
        file_entry.config(state="disabled")
        
        result = count_occurrences(file_path)
        if result:
            occurrences = result
            result_text = f"Occurrences:\n{occurrences}"
            result_label.config(text=result_text)
        else:
            result_label.config(text="Error occurred while processing the file.")

    
def count_occurrences(file_path):
    target_strings = [
        "Hello, my name is Peter Parker",
        "I love Python Programming", 
        "Love",
        "Enemy"
    ]
    
    try:
        with open(file_path, "r") as file:
            content = file.read()
        
        occurrences = {string: content.count(string) for string in target_strings}
        
        return occurrences
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    
    

#Create the main window

root = Tk()
root.title("String Counter App")

label = Label(root, text="Select a file: ")
label.pack(pady=10)

browse = Button(root, text="Browse", command=browse_file)
browse.pack()

file_entry = Entry(root, width=50, state="disabled")
file_entry.pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=10)

# Start the loop
root.mainloop()