import tkinter as tk
from tkinter import IntVar, StringVar, BooleanVar

main = tk.Tk()

def get_value():
    print(tk1.get())

tk1 = BooleanVar()
B1 = tk.Checkbutton(main, text="active", variable=tk1, command=get_value)
B1.pack()
main.mainloop()
