#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:57:05 2020

@author: pi
"""

from tkinter import *

def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return

master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind("<Button-1>",motion)
msg.pack()
mainloop()