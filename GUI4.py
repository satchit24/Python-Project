# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:56:17 2019

@author: Satchit
"""

from tkinter import *
from Inkwell import ink

window = Tk()

window.title("Photofilters")
 
window.geometry('350x200')
 
lbl = Label(window, text="Enter image name with extension")
txt = Entry(window,width=10)
txt.focus()
txt.grid(column=1, row=0)
iname=txt.get()
print (iname)
lbl.grid(column=0, row=0)

def inkclicked():
    img = io.imread("turtle.jpg")
    ink(img)
    
btn1 = Button(window, text="Inkwell", command=inkclicked) 
btn1.grid(column=1, row=1)

window.mainloop()