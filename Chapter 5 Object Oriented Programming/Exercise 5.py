import tkinter as tk
from tkinter import ttk, messagebox

class Animal:
    def __init__(self, animal_type, name, colour, age, weight, noise):
        self.type = animal_type
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
        self.noise = noise

    def say_hello(self):
        return f"{self.name} says hello!"

    def make_noise(self):
        return f"{self.name} makes a {self.noise} noise."

    def animal_details(self):
        return f"Type: {self.type}\nName: {self.name}\nColour: {self.colour}\nAge: {self.age}\nWeight: {self.weight}\nNoise: {self.noise}"

class AnimalGUI:
    def __init__(self, master):
        self.master = master
        master.title("Animal Interaction")

        # Create instances of Animal class
        self.dog = Animal("Dog", "Buddy", "Brown", 3, 15, "Woof")
        self.cow = Animal("Cow", "Daisy", "Black and White", 5, 800, "Moo")
        self.cat = Animal("Cat", "Whiskers", "Gray", 2, 10, "Meow")
        self.elephant = Animal("Elephant", "Dumbo", "Gray", 8, 5000, "Trumpet")
        self.owl = Animal("Owl", "Hedwig", "White", 4, 2, "Hoot")

        # Create style for ttk buttons
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), padding=10)

        # Create widgets
        self.label_animal = tk.Label(master, text="Select Animal:", font=('Helvetica', 14))
        self.label_animal.pack(pady=10)

        self.animal_var = tk.StringVar()
        self.animal_var.set("Dog")

        self.animal_menu = ttk.Combobox(master, textvariable=self.animal_var, values=["Dog", "Cow", "Cat", "Elephant", "Owl"])
        self.animal_menu.pack(pady=10)

        self.button_say_hello = ttk.Button(master, text="Say Hello", command=self.say_hello)
        self.button_make_noise = ttk.Button(master, text="Make Noise", command=self.make_noise)
        self.button_animal_details = ttk.Button(master, text="Animal Details", command=self.animal_details)

        self.button_say_hello.pack(pady=5)
        self.button_make_noise.pack(pady=5)
        self.button_animal_details.pack(pady=5)

    def say_hello(self):
        selected_animal = self.animal_var.get()
        animal_obj = getattr(self, selected_animal.lower())
        messagebox.showinfo("Say Hello", animal_obj.say_hello())

    def make_noise(self):
        selected_animal = self.animal_var.get()
        animal_obj = getattr(self, selected_animal.lower())
        messagebox.showinfo("Make Noise", animal_obj.make_noise())

    def animal_details(self):
        selected_animal = self.animal_var.get()
        animal_obj = getattr(self, selected_animal.lower())
        messagebox.showinfo("Animal Details", animal_obj.animal_details())

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimalGUI(root)
    root.mainloop()
