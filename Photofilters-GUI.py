# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:44:48 2019

@author: Satchit
"""
from tkinter import *
from Inkwell import *
from Sepia import *
from Gotham import *
from Nashville import *
from Poprocket import *
from Negative import *
from LOMOfi import *	
from Walden import *
from Cartoonifier import *

window = Tk()
 
window.title("Photofilters")
 
window.geometry('500x200')
 
lbl = Label(window, text="Enter file path")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.focus()
txt.grid(column=1, row=0)

def inkclicked():
    iname=txt.get()
    img = io.imread(iname)
    ink(img)
def sepiaclicked():
    iname=txt.get()
    img = io.imread(iname)
    sepia(img)
def gotclicked():
    iname=txt.get()
    img = io.imread(iname)
    gotham(img)
def nashclicked():
    iname=txt.get()
    img = io.imread(iname)
    nash(img)
def lomoclicked():
    iname=txt.get()
    img = io.imread(iname)
    lomo(img)
def negclicked():
    iname=txt.get()
    img = io.imread(iname)
    neg(img)
def popclicked():
    iname=txt.get()
    img = io.imread(iname)
    pop(img)
def waldclicked():
    iname=txt.get()
    img = io.imread(iname)
    wald(img)
def cartoonclicked():
    iname=txt.get()
    img = cv2.imread(iname)
    cartoon(img)
    
btn1 = Button(window, text="Inkwell", command=inkclicked) 
btn1.grid(column=1, row=1)
btn2 = Button(window, text="Gotham", command=gotclicked) 
btn2.grid(column=2, row=1)
btn3 = Button(window, text="Nashville", command=nashclicked) 
btn3.grid(column=3, row=1)
btn4 = Button(window, text="LOMO-fi", command=lomoclicked) 
btn4.grid(column=1, row=2)
btn5 = Button(window, text="Poprocket", command=popclicked) 
btn5.grid(column=2, row=2)
btn6 = Button(window, text="Sepia", command=sepiaclicked) 
btn6.grid(column=3, row=2) 
btn7 = Button(window, text="Negative", command=negclicked) 
btn7.grid(column=1, row=3)
btn8 = Button(window, text="Walden", command=waldclicked) 
btn8.grid(column=2, row=3)
btn9 = Button(window, text="Cartoonify", command=cartoonclicked) 
btn9.grid(column=3, row=3)

window.mainloop()