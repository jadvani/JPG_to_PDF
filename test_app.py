# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:35:50 2021

@author: Javier
"""
import tkinter
from tkinterdnd2 import *
import tkinterdnd2

from fpdf import FPDF
from PIL import Image

def export_to_pdf_app(files,pdfFileName, dir = ''):
    files = files.get().split(" ")
    pdfFileName = pdfFileName.get()
    if (dir):
        dir += "/"    
    cover = Image.open(files[0])
    width, height = cover.size
    pdf = FPDF(unit = "pt", format = [width, height])
    for page in files:
        pdf.add_page()
        pdf.image(page, 0, 0)
    pdf.output(dir + pdfFileName + ".pdf", "F")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
    
def drop(event):
    entry_sv.set(event.data)

root = tkinterdnd2.Tk(className='- JPG to PDF - ')

# # make the top right close button minimize (iconify) the main window
# root.protocol("WM_DELETE_WINDOW", root.iconify)
# # make Esc exit the program
# root.bind('<Escape>', lambda e: root.destroy())

# # create a menu bar with an Exit command
# menubar = tkinter.Menu(root)
# filemenu = tkinter.Menu(menubar, tearoff=0)
# filemenu.add_command(label="Exit", command=root.destroy)
# menubar.add_cascade(label="File", menu=filemenu)
# root.config(menu=menubar)

root.geometry("500x300")
root.wm_iconbitmap('logo.ico')
root.iconbitmap(r'logo.ico')

var = tkinter.IntVar()
a = tkinter.Label(root, text="PDF path")
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


button.wait_variable(var)
export_to_pdf_app(entry_sv,entry2)
a2 = tkinter.Label(root, text=" File(s) converted!")
a2.place(x=130, y=100)

root.mainloop()
