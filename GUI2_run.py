#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:43:46 2019
GUI2_BCT run file
@author: pi
"""

from Tkinter import Tk
from GUI2_BCT import *

ventana = Tk()
ventana.title("Prueba BCT")
ventana.geometry('1280x720')
#ventana.iconname
#ventana.resizable(True)
#ventana.iconbitmap('ProgGUI/GUI/resources/ICO/IconoBCT.ico')
app = GUI2_BCT(ventana)
ventana.protocol("WM_DELETE_WINDOW", app.cerrar)
ventana.mainloop()
ventana.destroy()