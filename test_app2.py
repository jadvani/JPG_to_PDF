# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:14:28 2021

@author: Javier
"""
import tkinter as tk
root = tk.Tk()
...
var = tk.IntVar()
button = tk.Button(root, text="Click Me", command=lambda: var.set(1))
button.place(relx=.5, rely=.5, anchor="c")

print("waiting...")
button.wait_variable(var)
print("done waiting.")
root.destroy()
