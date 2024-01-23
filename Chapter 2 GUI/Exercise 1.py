from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Exercise 1")
root.resizable(False , False)

welcome = Label(text="Welcome to my Exercise 1", font=("Helvetica", 20))
welcome.pack()

welcome.configure(bg="red")
root.configure(bg="green")


root.mainloop()