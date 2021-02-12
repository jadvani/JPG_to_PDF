# JPG Images to PDF: convert JPG files to PDF with a simple click!


This is a Python3-based app created using Tkinter to join and convert JPG files to PDF.

### Why did I created this app?

My old Samsung Laser Multifunction Printer scan images as single JPG images only. I use to scan lots of handwritten documents and I needed a tool to convert and classify these documents faster. It is well known that there are already some free web converters for this purpose, but these are limited to convert up to 5 or 10 pages each time, and you are not aware about the treatment they do to your information. It was also a good opportunity to get familiar with interface development using Python. instead of Qt Creator + C++. the only other framework I have ever used for these. 

With less than 65 lines of code in a single script, you will be able to run the converter and use it as many times as required. The execution finishes once you simply close the window!



![screenshot](https://github.com/jadvani/JPG_to_PDF/blob/main/img/screenshot_app.png)
 
 
These dependencies must be installed for its usage:

* PIL
* tkinter
* tkinterdnd2
* fpdf

 
Export the app as an .exe windows file using this command (pynstaller library must be available too for that):
pyinstaller --onefile --icon=logo.ico --noconsole test_app2.py


TODO:

* Add a button to choose the input files from path instead of the drag & drop way only.
* Add a button to choose the file output path
* improve the UX design somehow, add a background image to the interface.

