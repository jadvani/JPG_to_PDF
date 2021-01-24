# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:14:28 2021

# @author: Javier
# """
# import tkinter as tk
# root = tk.Tk()
# ...
# var = tk.IntVar()
# button = tk.Button(root, text="Click Me", command=lambda: var.set(1))
# button.place(relx=.5, rely=.5, anchor="c")

# print("waiting...")
# button.wait_variable(var)
# print("done waiting.")
# root.destroy()


import tkinter
from tkinter import messagebox
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


def drop(event):
    entry_sv.set(event.data)

root = tkinterdnd2.Tk(className='- JPG to PDF - ')
root.geometry("500x300")
root.wm_iconbitmap('logo.ico')

var = tkinter.IntVar()
a = tkinter.Label(root, text="PDF path")
a.place(x=10, y=50)
a0 = tkinter.Label(root, text=" ↑ Drop JPG files over the field above shown ↑")
a0.place(x=130, y=25)
entry_sv = tkinter.StringVar()
entry2_sv = tkinter.StringVar()
entry = tkinter.Entry(root, textvar=entry_sv, width=50)
entry.pack(fill=tkinter.X)
entry.drop_target_register(tkinterdnd2.DND_FILES)
entry.dnd_bind('<<Drop>>', drop)
entry2 = tkinter.Entry(root, textvar=entry2_sv, width=50)
entry2.place(x=100, y=50)

def convert_to_pdf():
   if(not entry_sv.get().strip() or not entry2.get().strip()):
       messagebox.showerror( "Error", "Please, drop the image file(s) to convert and its resulting PDF file name")
   else:
       export_to_pdf_app(entry_sv,entry2, dir = '')
       messagebox.showinfo( "- JPG to PDF - ", "File has been successfully created!")


B = tkinter.Button(root, text ="Convert to PDF", command = convert_to_pdf)
B.place(relx=.5, rely=.5, anchor="c")

root.mainloop()