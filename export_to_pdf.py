# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:11:20 2020

@author: Javier
"""

from fpdf import FPDF
from PIL import Image


def export_to_pdf(pdfFileName, listPages, dir = ''):
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]) + ".jpg")
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".jpg", 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")
    
def export_to_pdf_app(files,pdfFileName, dir = ''):
    if (dir):
        dir += "/"    
    cover = Image.open(files[0])
    width, height = cover.size
    pdf = FPDF(unit = "pt", format = [width, height])
    for page in files:
        pdf.add_page()
        pdf.image(page, 0, 0)

    pdf.output(dir + pdfFileName + ".pdf", "F")
        
    