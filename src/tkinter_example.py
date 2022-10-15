import tkinter as tk
from tkinter import Entry
root = tk.Tk()
root.geometry("300x200")

def func(event):
    print("You hit return.")

root.test = Entry(root)
root.test.bind('<Return>', func)
root.test.pack()

def onclick():
    print("You clicked the button")

button = tk.Button(root, text="click me", command=onclick)
button.pack()

root.mainloop()