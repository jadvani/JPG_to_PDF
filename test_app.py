# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:35:50 2021

@author: Javier
"""
import tkinter
from tkinterdnd2 import *
import tkinterdnd2

def drop(event):
    entry_sv.set(event.data)

root = tkinterdnd2.Tk(className='- JPG to PDF - ')
root.geometry("500x300")
var = tkinter.IntVar()
a = tkinter.Label(root, text="PDF result path")
a.place(x=10, y=50)
a0 = tkinter.Label(root, text=" ↑ Drop JPG files over the field above shown ↑")
a0.place(x=130, y=25)
entry_sv = tkinter.StringVar()
entry2_sv = tkinter.StringVar()
button = tkinter.Button(root, text="Convert to PDF", command=lambda: var.set(1))
button.place(relx=.5, rely=.5, anchor="c")
entry = tkinter.Entry(root, textvar=entry_sv, width=50)
entry.pack(fill=tkinter.X)
entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', drop)
entry2 = tkinter.Entry(root, textvar=entry2_sv, width=50)
entry2.place(x=100, y=50)
print("waiting...")
button.wait_variable(var)
print("done waiting.")
print(entry_sv.get())
print(entry2.get())
root.mainloop()
