#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:21:46 2020
Archivo: Reporte_PDF.py
Comentarios: Clase que implementa la creación de del informe del ensayo BCT
Versión: 2.0
@author: LFLQ
"""

import os
import commands

#Librerias reportlab a usar:
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import Frame as ReportFrame
from reportlab.platypus import (BaseDocTemplate, Paragraph, Table, 
                    NextPageTemplate, PageBreak, PageTemplate, Image, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
#from datetime import datetime

class PDF:
    def __init__(self):
        self.num_prueb = 0
        
        self.estilo=getSampleStyleSheet()
        self.estilo.add(ParagraphStyle(name='CuerpoJ', 
                                  fontName = "Times-Roman", 
                                  alignment= TA_JUSTIFY, 
                                  spaceAfter=2))
        self.estilo.add(ParagraphStyle(name='CuerpoC', 
                                  fontName = "Times-Roman", 
                                  alignment= TA_CENTER, 
                                  spaceAfter=2))
        self.story = []
#        for i in range(12):
#            self.story.append("")
        self.page_init = []
        
        #CREAMOS LOS FRAMES, para luego asignarlos a un pagetemplate.
        #===========================
        #Frame (x1, y1, ancho, alto, leftPadding=6, bottomPadding=6, rightPadding=6,
        # topPadding=6, id=None, showBoundary=0)
    
        #1. Frame que contendrá a toda el contenido de una hoja
        self.frameN = ReportFrame(cm*2.5, letter[1]-(25.5*cm), cm*17, 23.4*cm, id='normal')
        
        #2. Frame de columnas
        self.frame1 = ReportFrame(inch, inch, 220, 697, id='col1')
        self.frame2 = ReportFrame(inch + 230, inch, 220, 697, id='col2')
        
    def obtiene_fecha(self):
        months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        self.month = months[self.now.month - 1]
        self.tiempo = self.now.strftime('%H:%M')
        self.tiempoC = self.now.strftime('%H.%M')
        self.fecha = "{} de {} del {} a las ".format(self.now.day, self.month, self.now.year)
        self.fechaC= "{}-{}-{}".format(self.now.day, self.month, self.now.year)
        self.txt =str("Generado el día " + self.fecha + self.tiempo + ".")
        print self.txt
        
    def encabezado(self, canvas,doc):
        canvas.saveState()
        canvas.setFont('Times-Bold',14)
        canvas.drawString(cm*2.6, letter[1]-60+0.5*cm, 'Informe del ensayo BCT')
        canvas.setFont('Times-Italic',9)
        canvas.drawString(cm*2.6, letter[1]-60, self.txt)
        canvas.line(cm*2.6 , letter[1] - 65, letter[0] - 65, letter[1] - 65)
        logo = ImageReader('http://archimex.com.mx/img/archimex-logo-600.jpg')
        canvas.drawImage(logo, cm*13.7, letter[1]-64.33, 173.54, 56.70, mask='auto')
        canvas.restoreState()

    def pie(self, canvas,doc):
        canvas.saveState()
        canvas.setFont('Times-Roman',9)
        canvas.drawString(2.6*cm, letter[1]-(25.7*cm), 'Archimex Corrugados y Etiquetas S.A. de C.V.')
        canvas.drawString(2.6*cm, letter[1]-(26.1*cm), 'Kilometro 98.5 Carretera México-Puebla s/n,')
        canvas.drawString(2.6*cm, letter[1]-(26.5*cm), 'San sebastian Tepalcatepec Cholula, Puebla.')
        canvas.drawString(2.6*cm, letter[1]-(26.9*cm), 'C.P. 72760 Teléfono. 01222 141.52.00')
        canvas.drawString(letter[0]/2, letter[1]-(25.7*cm), "Página %d" % doc.page)
        logo1 = ImageReader('http://192.168.5.243/oee/__view/img/logo-final.png')
        canvas.drawImage(logo1, 17.5*cm, 0.75*cm, 2.09*cm, 1.80*cm, mask='auto')
        canvas.line(2.6*cm, letter[1]-(25.3*cm), letter[0]-60, letter[1]-(25.3*cm))
        canvas.restoreState()
        
    def add_PDF(self, t, BCTh, defor):
        self.tiemp = t
        self.Bh = BCTh
        self.Def = defor
            
        self.num_prueb += 1
        print "Número de prueba " + str(self.num_prueb) + " en PDF"
        self.story.append(Paragraph("Informe del ensayo de resistencia a la compresión (<b><i>BCT</i></b>) de la prueba {}.".format(self.num_prueb),
                                    self.estilo['Title']))                      
        
        self.story.append(NextPageTemplate('UnaColumna'))
        
        #***************** Agregar imagen ***************** 
        graf = Image('/home/pi/Desktop/InterfazG-BCT/resources/graf/GraficoBCT_{}.png'.format(self.num_prueb))
        self.story.append(graf)
        
        etiqueta_grafico = "<b><i>Gráfico {}.1.</i></b> Gráfico del ensayo de BCT de la prueba {}.".format(self.num_prueb, self.num_prueb)
        #self.story.append(Paragraph('-------', self.estilo['CuerpoC']))
        self.story.append(Paragraph(etiqueta_grafico, self.estilo['CuerpoC']))
        
        #***************** Tabla de datos ***************** 
        txt_tabla = "<b><i>Tabla {}.2.</i></b> Datos obtenidos del ensayo del BCT".format(self.num_prueb, self.num_prueb)
        self.story.append(Paragraph(txt_tabla, self.estilo['CuerpoJ']))
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
        self.story.append(t)
        #***************** Salto de página ***************** 
        self.story.append(PageBreak())
        
        #CREAMOS LOS PAGETEMPLATE, le asignamos los frames y los canvas
        #=================================
        #PageTemplate(id=None,frames=[],onPage=_doNothing,onPageEnd=_doNothing)
        self.PTUnaColumna = PageTemplate(id='UnaColumna', 
                                         frames=self.frameN, 
                                         onPage=self.encabezado, 
                                         onPageEnd=self.pie)
        '''self.PTDosColumnas= PageTemplate(id='DosColumnas', 
                                         frames=[self.frame1,self.frame2],
                                         onPage=self.encabezado, 
                                         onPageEnd=self.pie)'''
        
    def build_PDF(self):
        #CREAMOS EL DOCTEMPLATE, a partir del BaseDocTemplate
        self.obtiene_fecha()
        directorio = '/home/pi/Desktop/Reportes_Generados/{}'.format(self.now.year)
        if not os.path.isdir(directorio):
            directorio += '/{}'.format(self.month)
            commands.getoutput('mkdir /home/pi/Desktop/Reportes_Generados/{}'.format(self.now.year))
            if not os.path.isdir(directorio):
                commands.getoutput('mkdir /home/pi/Desktop/Reportes_Generados/{}/{}'.format(self.now.year, self.month))
                print 'Directorio creado con éxito'
        else:
            directorio += '/{}'.format(self.month)
            if not os.path.isdir(directorio):
                commands.getoutput('mkdir /home/pi/Desktop/Reportes_Generados/{}/{}'.format(self.now.year, self.month))
                print 'Directorio creado con éxito'
        #===============================
        self.direc = '/home/pi/Desktop/Reportes_Generados/{}/{}/BCT_reporte_{}_{}.pdf'.format(self.now.year, self.month, self.fechaC, self.tiempoC)
        doc = BaseDocTemplate(self.direc,
                              pageTemplates=[self.PTUnaColumna], 
                              #pageTemplates=[self.PTUnaColumna, self.PTDosColumnas], 
                              pagesize=letter)
        #Construimos el PDF  )
        self.page_init.append(self.t)
        self.page_init.append(self.story)
        doc.build(self.story)
        
    def load_data(self, largo, ancho, alto, prod, clie, datos):
        largoC = str(largo) + " cm"
        anchoC = str(ancho) + " cm"
        altoC = str(alto) + " cm"
        perC = str(largo+ancho+alto) + ' cm'
        data= [['Largo', 'Ancho', 'Alto', 'Perímetro'],
               [largoC, anchoC, altoC, perC]]
        data1=[['Estilo de\ncaja', 'Tipo de flauta', 'Dirección de\nla flauta', 'Grado del\nmaterial', 'Tipo de unión'],
               [datos[0],       datos[1],           datos[2],                   datos[3],               datos[4]]]
        data2=[['Método de cierre', 'Orientación de la prueba', 'Número de pruebas'],
               [datos[5],           datos[6],                   self.num_prueb]]
        
        # Titulo
        self.story[0] = (Paragraph("Informe del ensayo de resistencia a la compresión (<b><i>BCT</i></b>)", 
                                    self.estilo['Title']))
        
        # Cuerpo
        self.story[1] = (Paragraph("<b>Producto:</b> {}".format(prod)
                                    , self.estilo['CuerpoJ']))
        self.story[2] = (Paragraph("<b>Cliente:</b> {}".format(clie)
                                    , self.estilo['CuerpoJ']))
        
        etiqueta_grafico = "<b><i>Tabla 1.1.</i></b> Dimensiones de la caja."
        self.story[3] = (Paragraph(etiqueta_grafico, self.estilo['CuerpoC']))
        # Insertar la tabla con los datos de la variable 'data' (Dimensiones de la caja)
        self.t=Table(data)
        self.t.setStyle(TableStyle([('BACKGROUND',(0,0),(3,0),colors.darkorange),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black),
                               ('TEXTCOLOR',(0,0),(3,0),colors.whitesmoke),
                               ('BACKGROUND',(0,1),(-1,-1),colors.navajowhite),
                               ('TEXTCOLOR',(0,1),(3,1),colors.black),
                               ('ALIGN',(0,0), (-1,-1), 'CENTER')]))
        self.story[4] = (self.t)
        self.story[5] = (Paragraph('.', self.estilo['CuerpoC']))
        etiqueta_grafico = "<b><i>Tabla 1.2.</i></b> Descripción de la caja."
        self.story[6] = (Paragraph(etiqueta_grafico, self.estilo['CuerpoC']))
        # Insertar la tabla con los datos de la variable 'data'
        self.t1=Table(data1)
        self.t1.setStyle(TableStyle([('BACKGROUND',(0,0),(4,0),colors.darkorange),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black),
                               ('TEXTCOLOR',(0,0),(4,0),colors.whitesmoke),
                               ('BACKGROUND',(0,1),(-1,-1),colors.navajowhite),
                               ('TEXTCOLOR',(0,1),(4,1),colors.black),
                               ('ALIGN',(0,0), (-1,-1), 'CENTER'),
                               ('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
        self.story[7] = (self.t1)
        self.story[8] = (Paragraph('.', self.estilo['CuerpoC']))
        etiqueta_grafico = "<b><i>Tabla 1.3.</i></b> Descripción de la prueba."
        self.story[9] = (Paragraph(etiqueta_grafico, self.estilo['CuerpoC']))
        self.t2=Table(data2)
        self.t2.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.darkorange),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black),
                               ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                               ('BACKGROUND',(0,1),(-1,-1),colors.navajowhite),
                               ('TEXTCOLOR',(0,1),(-1,1),colors.black),
                               ('ALIGN',(0,0), (-1,-1), 'CENTER'),
                               ('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
        self.story[10] = (self.t2)
        # --------- SALTO DE PÁGINA --------------
        self.story[11] = (PageBreak())
        
    def reset_num(self, tiempo_ahora):
        self.now = tiempo_ahora
        self.num_prueb = 0
        for i in range(12):
            self.story.append("")
        print 'Número de prueba a cero'