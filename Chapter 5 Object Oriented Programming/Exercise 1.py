import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    @classmethod
    def oldest_dog(cls, dog1, dog2):
        oldest = dog1 if dog1.age > dog2.age else dog2
        messagebox.showinfo("Oldest Dog", f"The oldest dog is {oldest.name}, a {oldest.breed}.")

    def woof(self):
        messagebox.showinfo("Woof!", f"{self.name} says Woof!")

class DogGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dog GUI")

        # Dog instances
        self.dog1 = Dog("Aldrin", 4, "Golden Shepherd")
        self.dog2 = Dog("Albert", 2, "German Soldier")

        # Display Dog Information Button
        self.display_button = tk.Button(master, text="Display Dog Info", command=self.display_info)
        self.display_button.pack(pady=10)

        # Woof Button
        self.woof_button = tk.Button(master, text="Oldest Dog Woof", command=self.oldest_dog_woof)
        self.woof_button.pack(pady=10)

    def display_info(self):
        messagebox.showinfo("Dog Information",
                            f"Dog 1: {self.dog1.name}, {self.dog1.age} years old, {self.dog1.breed}\n"
                            f"Dog 2: {self.dog2.name}, {self.dog2.age} years old, {self.dog2.breed}")

    def oldest_dog_woof(self):
        Dog.oldest_dog(self.dog1, self.dog2)
        oldest_dog = self.dog1 if self.dog1.age > self.dog2.age else self.dog2
        oldest_dog.woof()

if __name__ == "__main__":
    root = tk.Tk()
    app = DogGUI(root)
    root.mainloop()
