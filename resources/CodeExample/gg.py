#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:50:27 2020

@author: pi
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader

logo = ImageReader('https://www.google.com/images/srpr/logo11w.png')

canvas = Canvas('output.pdf', pagesize=letter)
canvas.drawImage(logo, 10, 10, mask='auto')
canvas.showPage()
canvas.save()