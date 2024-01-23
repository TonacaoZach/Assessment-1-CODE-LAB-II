from tkinter import *

root = Tk()
root.geometry("500x333")
def getvals():
    print (f"Name {uservalue.get()}")
    print (f"Phone {phonevalue.get()}")
    print (f"Gender {gendervalue.get()}")
    print (f"Emergency Contact {contactvalue.get()}")
    print (f"Payment Mode {paymentvalue.get()}")
    print (f"Food Service {foodservicevalue.get()}")


user = Label(root, text="Name", font=("Arial", 15))
phone = Label(root, text="Phone", font=("Arial", 15))
gender = Label(root, text="Gender", font=("Arial", 15))
contact = Label(root, text="Emergency Contact", font=("Arial", 15))
payment = Label(root, text="Payment Mode", font=("Arial", 15))
user.grid(row=3, column=2)
phone.grid(row=4, column=2)
gender.grid(row=5, column=2)
contact.grid(row=6, column=2)
payment.grid(row=7, column=2)

Member = Label(root, text="Membership Form", font=("Arial", 15), pady=10)

Member.grid(row=1, column=3)


uservalue = StringVar()
phonevalue = IntVar(value="+971")
gendervalue = StringVar()
contactvalue = IntVar(value="+971")
paymentvalue = StringVar()
foodservicevalue = BooleanVar()

userentry = Entry(root, textvariable=uservalue, width=20, font=("Arial", 15))
phoneentry = Entry(root, textvariable=phonevalue, width=20, font=("Arial", 15))
genderentry = Entry(root, textvariable=gendervalue, width=20, font=("Arial", 15))
contactentry = Entry(root, textvariable=contactvalue, width=20, font=("Arial",15))
paymententry = Entry(root, textvariable=paymentvalue, width=20, font=("Arial", 15))


userentry.grid(row=3, column=3)
phoneentry.grid(row=4, column=3)
genderentry.grid(row=5, column=3)
contactentry.grid(row=6, column=3)
paymententry.grid(row=7, column=3)

foodservice = Checkbutton(root, text="Want to prebook your seat?", font=("Arial", 15), variable=foodservicevalue)
foodservice.grid(row=8, column=3)

button = Button(root, text="Submit", command=getvals, font=("Arial", 15))
button.grid(row=9, column=3)

root.mainloop()