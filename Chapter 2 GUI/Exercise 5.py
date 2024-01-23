from tkinter import *

root = Tk()

root.title("Calculator")

inp = Entry(root, width=35, borderwidth=7) #input the number
inp.grid(row=0, column=0, columnspan=3, padx=15, pady=15) #displays the box

def button_click(num):
    current = inp.get()
    inp.delete(0, END)
    inp.insert(0, str(current) + str(num))
    
def button_clear():
    inp.delete(0, END)

def button_add():
    first_num = inp.get()
    global num1
    global oper
    oper = "add"
    num1 = int(first_num)
    inp.delete(0, END)

def button_sub():
    first_num = inp.get()
    global num1
    global oper
    oper = "sub"
    num1 = int(first_num)
    inp.delete(0, END)

def button_mul():
    first_num = inp.get()
    global num1
    global oper
    oper = "mul"
    num1 = int(first_num)
    inp.delete(0, END)

def button_div():
    first_num = inp.get()
    global num1
    global oper
    oper = "div"
    num1 = int(first_num) #turns the number into an integer
    inp.delete(0, END)

def button_equals():
    second_num = inp.get()
    inp.delete(0, END)

    if oper == "add":
        inp.insert(0, num1 + int(second_num))
        
    if oper == "sub":
        inp.insert(0, num1 - int(second_num))
      
    if oper == "mul":
        inp.insert(0, num1 * int(second_num))    
        
    if oper == "div":
        inp.insert(0, num1 / int(second_num))
        



#program the buttons

button_1 = Button(root, text="1", padx = 40, pady = 20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx = 40, pady = 20, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx = 40, pady = 20, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx = 40, pady = 20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx = 40, pady = 20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx = 40, pady = 20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx = 40, pady = 20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx = 40, pady = 20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx = 40, pady = 20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx = 40, pady = 20, command= lambda: button_click(0))
button_add = Button(root, text="+", padx = 39, pady = 20, command= button_add)
button_sub = Button(root, text="- ", padx = 40, pady = 20, command= button_sub)
button_mul = Button(root, text="x", padx = 40, pady = 20, command= button_mul)
button_div = Button(root, text="÷", padx = 39, pady = 20, command= button_div)
button_clear = Button(root, text="Clear", padx = 30, pady = 20, command= button_clear)
button_equals = Button(root, text="=", padx = 135, pady = 20, command= button_equals)

#display the buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)

button_clear.grid(row=5,column=0)
button_mul.grid(row=5,column=1)
button_div.grid(row=5,column=2)

button_equals.grid(row=6, column=0, columnspan=3)




root.mainloop() #calls the program and runs it