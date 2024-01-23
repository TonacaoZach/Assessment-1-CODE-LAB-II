from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("Exercise with Pack")

left_frame = Frame(root, borderwidth=5)
right_frame = Frame(root, borderwidth=5)


left_frame.pack(side="left", fill="both", expand=True)
right_frame.pack(side="right", fill="both", expand=True)


label_a = Label(left_frame, text="A", bg="#2E4CC4", fg="white")
label_b = Label(left_frame, text="B", bg="white", fg="#2E4CC4")

label_a.pack(side="top", fill="both", expand=True)
label_b.pack(side="bottom", fill="both", expand=True)

label_c = Label(right_frame, text="C", bg="White", fg="#2E4CC4")
label_d = Label(right_frame, text="D", bg="#2E4CC4", fg="white")

label_c.pack(side="top", fill="both", expand=True)
label_d.pack(side="bottom", fill="both", expand=True)

root.mainloop()