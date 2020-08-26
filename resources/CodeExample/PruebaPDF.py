#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:21:46 2020
Archivo: PruebaPDF.py
Comentarios: Archivo para entender ReportLab
@author: pi
"""

#-*- coding:utf-8 -*-
import os

#Librerias reportlab a usar:
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, Frame, Paragraph,  
                    NextPageTemplate, PageBreak, PageTemplate)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from datetime import datetime

# Hola sublime
#NIVEL 1: CREAMOS LOS CANVAS
#===========================   
#Creamos los canvas para el pie de página y encabezado, que serán fijos
def encabezado(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',14)
    canvas.drawString(cm*2.6, letter[1]-60+0.5*cm, 'Reporte de la prueba BCT')
    canvas.setFont('Times-Italic',9)
    now = datetime.now()
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    month = months[now.month - 1]
    tiempo = now.strftime('%H:%M')
    fecha = "{} de {} del {} a las ".format(now.day, month, now.year)
    txt =str("Generado el día " + fecha + tiempo + ".")
    canvas.drawString(cm*2.6, letter[1]-60, txt)
    canvas.line(cm*2.6 , letter[1] - 65, letter[0] - 65, letter[1] - 65)
    logo = ImageReader('http://archimex.com.mx/img/archimex-logo-600.jpg')
    canvas.drawImage(logo, cm*13.7, letter[1]-64.33, 173.54, 56.70, mask='auto')
    canvas.restoreState()
    
def pie(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(2.6*cm, letter[1]-(25.7*cm), "Página %d" % doc.page)
    logo1 = ImageReader('http://192.168.5.243/oee/__view/img/logo-final.png')
    canvas.drawImage(logo1, 17.5*cm, 0.75*cm, 2.09*cm, 1.80*cm, mask='auto')
    canvas.line(2.6*cm, letter[1]-(25.3*cm), letter[0]-60, letter[1]-(25.3*cm))
    canvas.restoreState()

#NIVEL 2: CREAMOS LOS FLOWABLES
#==============================
#Creamos la hoja de Estilo
estilo=getSampleStyleSheet()
estilo.add(ParagraphStyle(name='CuerpoJ',
               fontName = "Times-Roman", alignment= TA_JUSTIFY, spaceAfter=2))
estilo.add(ParagraphStyle(name='CuerpoC',
               fontName = "Times-Roman", alignment= TA_CENTER, spaceAfter=2))

#Iniciamos el platypus story
story=[]
story.append('')

#Añadimos al story los flowables. Hay que tener en cuenta que se inicia
#con el primer pageTemplate "UnaColumna"
story.append(Paragraph("Esto es el texto del Frame normal del pagetemplate" +\
                       " de una columna"* 500, estilo['CuerpoJ']))
                        
story.append(NextPageTemplate('DosColumnas'))  # Cambio de PageTemplate
story.append(PageBreak())  # Inicio en otra hoja
story.append(Paragraph("Esto es el texto del Frame que pertenece al" +\
                       " pagetemplate de dos columnas" * 500, estilo['Normal']))
                
story.append(NextPageTemplate('UnaColumna'))
story.append(PageBreak())
story[0]=(Paragraph("Regresamos al texto del Frame normal del" +\
                        " pagetemplate de dos columnas"*100, estilo['Normal']))

#NIVEL 3: CREAMOS LOS FRAMES, para luego asignarlos a un pagetemplate.
#===========================
#Frame (x1, y1, ancho, alto, leftPadding=6, bottomPadding=6, rightPadding=6,
# topPadding=6, id=None, showBoundary=0)

#1. Frame que contendrá a toda el contenido de una hoja
frameN = Frame(cm*2.5, letter[1]-(25.5*cm), cm*17, 23.4*cm, id='normal')
print str(cm*18)
#2. Frame de columnas
frame1 = Frame(inch, inch, 220, 697, id='col1')
frame2 = Frame(inch + 230, inch, 220, 697, id='col2')

#NIVEL 4: CREAMOS LOS PAGETEMPLATE, le asignamos los frames y los canvas
#=================================
#PageTemplate(id=None,frames=[],onPage=_doNothing,onPageEnd=_doNothing)
PTUnaColumna = PageTemplate(id='UnaColumna', frames=frameN, onPage=encabezado, onPageEnd=pie)
PTDosColumnas =  PageTemplate(id='DosColumnas', frames=[frame1,frame2],
                        onPage=encabezado, onPageEnd=pie)

#NIVEL 5: CREAMOS EL DOCTEMPLATE, a partir del BaseDocTemplate
#===============================
doc = BaseDocTemplate('test.pdf', pageTemplates=[PTUnaColumna, PTDosColumnas], 
        pagesize=letter)

#Construimos el PDF
doc.build(story)

os.system("test.pdf")