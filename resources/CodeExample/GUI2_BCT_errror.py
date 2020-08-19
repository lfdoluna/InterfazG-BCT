#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:04:37 2019
Modificacion GUI_BCT.py a python 2.7
@author: pi
"""
#IMPORTAMOS LIBRERIAS NECESARIAS.
from Tkinter import *
import tkMessageBox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as animation
from datetime import datetime
from wFile import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from Reporte_PDF import *
import commands
import RPi.GPIO as GPIO
#from MotorPAP import *
 
class GUI2_BCT_errror:
    def __init__(self, maestro):
        #GPIO.setmode(GPIO.BOARD)
        self.banderaMD = False
        self.banderaMI = False
        '''self.control_pins = [3,5,7]
        for pin in self.control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)'''
        #self.AccM = MotorPAP()
        
        #Esquema del marco
        self.marco = Frame(maestro)
        self.marco.grid()
        
        style.use("ggplot")
        self.bandera = False
        self.fW = wFile()
        self.docPDF = Reporte_PDF()
        self.num_prueb = 0
        self.xyValue = []
        self.tempor = 0
        
        #------------------------------CREAR GRAFICA---------------------------------
        self.fig = Figure(figsize=(10.24, 4.35), dpi=100)
        self.a = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self.marco)  # CREAR AREA DE DIBUJO DE TKINTER.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row = 0, column = 0, columnspan = 4)
        
        #-------------------GUI (Botones, etiquetas y textbox)-------------------------
        self.pdfB = Button(self.marco, text = "Generar informe\nPDF", command = self.exportPDF)
        self.pdfB.grid(row = 1, column = 3, sticky ="w")
        #Inicializar imagenes
        self.imgbtnAr = PhotoImage(file = 'ProgGUI/GUI/flechaArriba.png')
        self.imgbtnAb = PhotoImage(file = 'ProgGUI/GUI/flechaAbajo.png')
        self.imgbtnPa = PhotoImage(file = 'ProgGUI/GUI/botonR.png')
        self.imgbtnArr= PhotoImage(file = 'ProgGUI/GUI/botonV.png')
        self.imgbtnRe = PhotoImage(file = 'ProgGUI/GUI/reiniciar.png')
        
        # Botón cerrar
        self.button = Button(self.marco, text="CERRAR", command=self.cerrar, fg="white", bg = 'red')
        self.button.grid(row = 1, column = 3, sticky ="e")
        
        # Botón arriba
        self.arrB = Button(self.marco, image = self.imgbtnAr)
        self.arrB ['command'] = self.Arriba
        self.arrB.grid(row = 1, column = 0)
        
        # Botón abajo
        self.abaB = Button(self.marco, image = self.imgbtnAb)
        self.abaB ['command'] = self.Abajo
        self.abaB.grid(row = 2, column = 0)
        
        #etiquetas para instrucciones
        self.instruccion = Label(self.marco, text='BCT')
        self.instruccion.grid(row = 1, column = 1, sticky = "n")
        
        #Combobox para respuesta
        self.txtBCT = Text(self.marco, width = 20, height = 2, wrap = WORD)
        self.txtBCT.grid(row =1, column = 1, sticky = "s")
        
        #etiquetas para instrucciones
        self.instruccionP = Label(self.marco, text='Desplazamiento')
        self.instruccionP.grid(row = 1, column = 2, sticky = "n")
        
        #Combobox para respuesta
        self.txtPos = Text(self.marco, width = 20, height = 2, wrap = WORD)
        self.txtPos.grid(row =1, column = 2, sticky = "s")
                
        #Boton de inicio de prueba
        self.StartB = Button(self.marco, image = self.imgbtnArr)
        self.StartB ['command'] = self.StartG
        self.StartB.grid(row = 2, column = 1)
        
        #Boton de reset de prueba
        self.ResetB = Button(self.marco, image = self.imgbtnRe)
        self.ResetB ['command'] = self.resetFile
        self.ResetB.grid(row = 2, column = 2)
        
        #Boton de paro de prueba
        self.StopB = Button(self.marco, image = self.imgbtnPa,text = 'Paro')
        self.StopB ['command'] = self.StopG
        self.StopB.grid(row = 2, column = 3)
        
        #-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
        self.toolbarFrame = Frame(self.marco)
        self.toolbarFrame.grid(row = 3,column = 0, columnspan = 4)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)
        self.toolbar.grid(row = 4, column = 0, columnspan = 4)
        
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=500)
        
        self.resetFile(False)
        
    def Arriba(self):
        if self.banderaMI == True:
            self.banderaMD = True
            self.banderaMI = False
            '''GPIO.output(5, 0)
            GPIO.output(3, 1)'''
            print "Boton arriba pulsado cuando abajo esta pulsado"
        elif self.banderaMD == False:
            self.banderaMD = True
            #GPIO.output(3, 1)
            print "Boton arriba pulsado"
        else:
            self.banderaMD = False
            #GPIO.output(3, 0)
            print "Boton arriba pulsado de nuevo"
            
    def Abajo(self):
        if self.banderaMD == True:
            self.banderaMI = True
            self.banderaMD = False
            '''GPIO.output(3, 0)
            GPIO.output(5, 1)'''
            print "Boton abajo pulsado cuando arriba esta pulsado"
        elif self.banderaMI == False:
            self.banderaMI = True
            #GPIO.output(5, 1)
            print "Boton abajo pulsado"
        else:
            self.banderaMI = False
            #GPIO.output(5, 0)
            print "Boton abajo pulsado de nuevo"

    def exportPDF(self):
        if self.bandera == True:
            self.StopG()
            tkMessageBox.showerror("Atención","Se detuvo la prueba por seguridad")
        if self.num_prueb == 0:
            tkMessageBox.showinfo('Atención', 'Debe realizar la prueba antes de exportar los datos')
        else:
            desp = float(self.xyValue[0])*0.005
            if self.num_prueb == 1:
                #self.docPDF.crea(True, self.segundos, self.xyValue[2], desp)
                self.docPDF.add_PDF(self.segundos, self.xyValue[2], desp)
            else:
                #self.docPDF.crea(False, self.segundos, self.xyValue[2], desp)
                self.docPDF.add_PDF(self.segundos, self.xyValue[2], desp)
            answ=tkMessageBox.askyesno("Atención", "Datos recopilados en PDF, ¿Desea realizar otra pueba?")
            if answ==False:
                self.resetFile(False)
                self.docPDF.buid_PDF()
                self.num_prueb = 0
                respuesta=tkMessageBox.askyesno("Reporte creado", "Reporte creado con éxito, ¿Desea abrir el reporte?")
                if respuesta==True:
                    commands.getoutput('qpdfview BCT_reporte.pdf')
            else:
                self.resetFile(False)

    def cerrar(self):
        if self.bandera == True:
            self.StopG()
            tkMessageBox.showerror("Atención","Se detuvo la prueba por seguridad")
        respuesta=tkMessageBox.askyesno("Cuidado", "¿Quiere salir del programa?")
        if respuesta==True:
            #sys.exit()
            self.resetFile(False)
            GPIO.cleanup()
            self.marco.quit()
        
    def animate(self,i):
        if self.bandera == True:
            self.xyValue = self.fW.EscribeArch()
            print(str(self.xyValue) + " Animate")
            pullData = open("ProgGUI/GUI/sampleText.txt","r").read()
            dataList = pullData.split('\n')
            self.xList = []
            self.yList = []
            for eachLine in dataList:
                if len(eachLine) > 1:
                    x, y = eachLine.split(',')
                    self.xList.append(float(x))
                    self.yList.append(float(y))
            self.a.clear()
            self.a.plot(self.xList, self.yList)
            self.a.set_ylabel("BCT (kg)")
            self.a.set_xlabel('Desplazamiento (mm)')
            self.tempor += 1
            self.esctxtCB()
        else:
            self.a.clear()
            self.a.set_ylabel("BCT (kg)")
            self.a.set_xlabel('Desplazamiento (mm)')
            
    def resetFile(self, edo = True):
        if edo == True:
            respuesta=tkMessageBox.askyesno("Cuidado", "¿Desea reiniciar la prueba actual?")
            if respuesta==True:
                self.ani.event_source.start()
                self.xyValue = self.fW.EscribeArch(True)
                print(str(self.xyValue) + " resetFile")
                self.esctxtCB()
                self.bandera = False
                self.StopG()
        else:
            self.ani.event_source.start()
            self.xyValue = self.fW.EscribeArch(True)
            print(str(self.xyValue) + " resetFile")
            self.esctxtCB()
            self.bandera = False
                
    def StartG(self):
        respuesta=tkMessageBox.askyesno("Cuidado", "¿Está seguro de iniciar la prueba?")
        if respuesta==True:
            #GPIO.output(7, 1)
            self.num_prueb += 1
            self.instanteInicial = datetime.now()
            if self.bandera == False:
                self.ani.event_source.start() #INICIA/REANUDA ANIMACIÓN
                self.bandera = True
            
    def StopG(self):
        if self.bandera == True:
            self.ani.event_source.stop() #DETIENE ANIMACIÓN
            self.instanteFinal = datetime.now()
            tiempo = self.instanteFinal - self.instanteInicial 
            self.segundos = tiempo.seconds
            self.bandera = False
        plt.ioff()
        #GPIO.output(7, 0)
        figs = plt.figure()
        pltAr = figs.add_subplot(111)
        pltAr.plot(self.xList, self.yList)
        plt.xlabel('Desplazamiento (mm)')
        plt.ylabel("BCT (kg)")
        plt.savefig('ProgGUI/GUI/GraficoBCT.png')
        print("Grafico creado")
        plt.clf()
        
            
    def esctxtCB(self):
        self.txtBCT.delete(0.0, END)
        self.txtBCT.insert(0.0, self.xyValue[1])
        self.txtPos.delete(0.0, END)
        self.txtPos.insert(0.0, self.xyValue[0])