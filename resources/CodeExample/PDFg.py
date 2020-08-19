#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:39:54 2019
Archivo: testerPDF1.py
Versión = 1.0
@author: pi
"""
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime

class PDFg():
    def __init__(self):
        # Elements sirve para agregar txt, imagenes, tablas
        self.elements = []
        # Importación de estilos de letras
        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='CuerpoJ',
               fontName = "Times-Roman", alignment= TA_JUSTIFY, spaceAfter=2))
        self.styles.add(ParagraphStyle(name='CuerpoC',
               fontName = "Times-Roman", alignment= TA_CENTER, spaceAfter=2))
        self.styleH = self.styles['Title']
        self.styleN = self.styles['BodyText']
        
    def crea(self, flag_start, t, BCTh, defor):
        self.tiemp = t
        self.Bh = BCTh
        self.Def = defor
        self.i = 1
        if flag_start == True:
            # Importación y formateo de la fecha y hora
            now = datetime.now()
            months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
            month = months[now.month - 1]
            tiempo = now.strftime('%H:%M')
            fecha = "{} de {} del {} a las ".format(now.day, month, now.year)
            txt =str("Reporte generado el día " + fecha + tiempo + ".")
        
            '''# Importación de estilos de letras
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='CuerpoJ',
               fontName = "Times-Roman", alignment= TA_JUSTIFY, spaceAfter=2))
            styles.add(ParagraphStyle(name='CuerpoC',
               fontName = "Times-Roman", alignment= TA_CENTER, spaceAfter=2))
            styleH = styles['Title']
            styleN = styles['BodyText']'''
            
            # Inicialización de imagenes
            logoA = Image('ProgGUI/GUI/Archimex.png', 260, 80)
            #graf = Image('ProgGUI/GUI/GraficoBCT.png', 500,300)
            
            logobj = [(logoA,"")]
            logo_table = Table(logobj, [2, 5.4])
            
            
            self.doc = SimpleDocTemplate("BCT_reporte.pdf", pagesize=letter,
            rightMargin=72,leftMargin=72, topMargin=18,bottomMargin=18)
            
            
            # Encabezado con imagenes
            self.elements.append(logo_table)
            
            # Insertar titulo del reporte
            self.elements.append(Paragraph("Reporte de la prueba BCT",self.styleH))
            
            # Insertar fecha y hora como tabla, alineando a la derecha
            self.elements.append(Paragraph(txt, self.styles['CuerpoJ']))
            #elements.append(Spacer(1,20))
            
        graf = Image('ProgGUI/GUI/GraficoBCT.png', 500,300)
        # Insertar cuerpo del reporte
        #elements.append(Paragraph("This is a paragraph in <i>Normal</i> style.", styleN))
        self.elements.append(graf)
        
        etiqueta_grafico = "<b><i>Gráfico {}.1.</i></b> Gráfico del ensayo de BCT de la prueba {}.".format(self.i, self.i)
        #elements.append(Paragraph("<b><i>Gráfico 1</i></b> Gráfico de la prueba de BCT.", styles['CuerpoC']))
        self.elements.append(Paragraph(etiqueta_grafico, self.styles['CuerpoC']))
        txt_tabla = "<b><i>Tabla {}.2.</i></b> Datos obtenidos del ensayo del BCT".format(self.i, self.i)
        self.elements.append(Paragraph(txt_tabla, self.styles['CuerpoJ']))
        
        # Obtención de datos
        s = str(self.tiemp) + " s"
        kg = str(self.Bh) + " Kg"
        mm = str(self.Def) + " mm"
        data= [['Tiempo', 'Valor BCT mas alto', 'Deformación'],
               [s, kg, mm]]
        
        # Insertar la tabla con los datos de la variable 'data'
        t=Table(data)
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(2,0),colors.darkorange),
                               ('GRID', (0, 0), (2, 1), 1, colors.black),
                               ('TEXTCOLOR',(0,0),(2,0),colors.whitesmoke),
                               ('BACKGROUND',(0,1),(-1,-1),colors.navajowhite),
                               ('TEXTCOLOR',(0,1),(2,1),colors.black),
                               ('ALIGN',(0,1), (-1,-1), 'CENTER')]))
        self.elements.append(t)
        
        # Iteración del numero de pruebas
        self.i += 1
        
    def genera_PDF(self):
        # Escribir elements en el documento
        self.doc.build(self.elements)