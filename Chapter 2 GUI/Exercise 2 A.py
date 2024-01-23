from tkinter import *
root = Tk()
root.geometry("300x100")
root.title("Exercise 2a")
root.resizable(False, False)

top = Frame(root)
top.pack(side = "top", fill="x")

w1 = Label(top, text="A", justify="center", bg="red", bd="5", relief="sunken")
w1.pack(fill="x")

middle = Frame(root)
middle.pack(side = "top", fill="x")

w3 = Label(middle, text="C", justify="center", bg="blue", bd="5")
w3.pack(side="left", fill="both", expand="yes")

w4 = Label(middle, text="D", justify="center", bg="white", bd="5")
w4.pack(side="right", fill="both", expand="yes")

w2 = Label(root, text="B", justify="center", bg="yellow", bd="5")
w2.pack(fill="x", )


root.mainloop()