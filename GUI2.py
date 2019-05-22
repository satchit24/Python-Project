# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:46:42 2019

@author: Satchit
"""
from Inkwell import *	
from tkinter import *
 
window = Tk()
 
window.title("Photofilters")
 
window.geometry('350x200')
 
lbl = Label(window, text="Enter image name with extension")
txt = Entry(window,width=10)
txt.grid(column=1, row=0)


lbl.grid(column=0, row=0)
 
def inkclicked():
    iname=txt.get()
    img = io.imread(iname)
    ink(img)
 
btn1 = Button(window, text="Inkwell", command=inkclicked) 
btn1.grid(column=1, row=1)

btn1 = Button(window, text="Inkwell", command=inkclicked) 
btn1.grid(column=1, row=1)
btn1 = Button(window, text="Inkwell", command=inkclicked) 
btn1.grid(column=1, row=1)
btn1 = Button(window, text="Inkwell", command=inkclicked) 
btn1.grid(column=1, row=1) 
window.mainloop()