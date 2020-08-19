#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:04:37 2019
Modificacion GUI_BCT.py a python 2.7
@author: pi
"""
#IMPORTAMOS LIBRERIAS NECESARIAS.
from Tkinter import PhotoImage,\
                    Button,\
                    Label,\
                    Text,\
                    Frame,\
                    END,\
                    WORD
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
from wFile import *
from PDF import *
from DATAin import *
from VentanaFinal import *
import commands
import os.path as path
import RPi.GPIO as GPIO
import tkMessageBox
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

class GUI2_BCT:
    def __init__(self, maestro):
        self.master = maestro
        #GPIO.setmode(GPIO.BOARD)
        self.banderaMD = False
        self.banderaMI = False
        '''self.control_pins = [3,5,7]
        for pin in self.control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)'''
        #self.AccM = MotorPAP()
        
        #Esquema del marco
        #self.marco = Frame(maestro)
        self.marco1 = maestro
        self.marco1.grid()
        #self.marco1.resizable(True)
        
        style.use("ggplot")
        self.bandera = False
        
        # IMPORTACIÖN DE LAS CLASES 
        self.fW = wFile()
        self.docPDF = PDF()
        
        self.num_prueb = 0
        self.num_pruebaR = False
        self.xyValue = []
        self.tempor = 0
        
        #------------------------------CREAR GRAFICA---------------------------------
        self.fig = Figure(figsize=(12.8, 4.8), dpi=100)
        self.a = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self.marco1)  # CREAR AREA DE DIBUJO DE TKINTER.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row = 0, column = 0, columnspan = 5)
        
        #-------------------GUI (Botones, etiquetas y textbox)-------------------------
        self.pdfB = Button(self.marco1, text = "Generar informe\nPDF", command = self.exportPDF)
        self.pdfB.grid(row = 1, column = 3)
        #Inicializar imagenes
        self.imgbtnAr = PhotoImage(file = '/home/pi/Desktop/ProgGUI/GUI/resources/img/button/flechaArriba.png')
        self.imgbtnAb = PhotoImage(file = '/home/pi/Desktop/ProgGUI/GUI/resources/img/button/flechaAbajo.png')
        self.imgbtnPa = PhotoImage(file = '/home/pi/Desktop/ProgGUI/GUI/resources/img/button/botonR.png')
        self.imgbtnArr= PhotoImage(file = '/home/pi/Desktop/ProgGUI/GUI/resources/img/button/botonV.png')
        self.imgbtnRe = PhotoImage(file = '/home/pi/Desktop/ProgGUI/GUI/resources/img/button/reiniciar.png')
        
        # Botón cerrar
        self.button = Button(self.marco1, text="CERRAR", command=self.cerrar, fg="white", bg = 'red')
        self.button.grid(row = 1, column = 4)
        
        # Botón arriba
        self.arrB = Button(self.marco1, image = self.imgbtnAr)
        self.arrB ['command'] = self.Arriba
        self.arrB.grid(row = 1, column = 0)
        
        # Botón abajo
        self.abaB = Button(self.marco1, image = self.imgbtnAb)
        self.abaB ['command'] = self.Abajo
        self.abaB.grid(row = 2, column = 0)
        
        #etiquetas para instrucciones
        self.instruccion = Label(self.marco1, text='BCT')
        self.instruccion.grid(row = 1, column = 1, sticky = "n")
        
        #Combobox para respuesta
        self.txtBCT = Text(self.marco1, width = 20, height = 2, wrap = WORD)
        self.txtBCT.grid(row =1, column = 1, sticky = "s")
        
        #etiquetas para instrucciones
        self.instruccionP = Label(self.marco1, text='Desplazamiento')
        self.instruccionP.grid(row = 1, column = 2, sticky = "n")
        
        #Combobox para respuesta
        self.txtPos = Text(self.marco1, width = 20, height = 2, wrap = WORD)
        self.txtPos.grid(row =1, column = 2, sticky = "s")
                
        #Boton de inicio de prueba
        self.StartB = Button(self.marco1, image = self.imgbtnArr)
        self.StartB ['command'] = self.StartG
        self.StartB.grid(row = 2, column = 1)
        
        #Boton de reset de prueba
        self.ResetB = Button(self.marco1, image = self.imgbtnRe)
        self.ResetB ['command'] = self.resetFile
        self.ResetB.grid(row = 2, column = 2)
        
        #Boton de paro de prueba
        self.StopB = Button(self.marco1, image = self.imgbtnPa,text = 'Paro')
        self.StopB ['command'] = self.StopG
        self.StopB.grid(row = 2, column = 3)
        
        #Boton para iniciar ventana donde se agregan datos de la caja
        self.ventanaIN = Button(self.marco1,text = 'Ingrese datos\n de la caja')
        self.ventanaIN['command'] = self.ventanaDATA
        self.ventanaIN.grid(row = 2, column = 4)
        
        #-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
        self.toolbarFrame = Frame(self.marco1)
        self.toolbarFrame.grid(row = 3,column = 0, columnspan = 5)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)
        self.toolbar.grid(row = 4, column = 0, columnspan = 4)
        
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=500)
        
        self.gg = True      #Bandera de actividad de la ventana de ingreso de datos
        self.banderaDATA = False #Bandera de ingreso de datos
        self.alturaC = 0
        self.anchoC = 0
        self.largoC = 0
        self.InfoCj = []
        self.resetFile(False)
        
    def ventanaDATA(self):
        self.banderaDATA = True
        if self.gg == True:
            print 'Hola ventana'
            #self.marco1.iconify()
            self.marco2 = DATAin(self.master)
            #self.marco1.wait_window(self.marco2.top)
            self.gg = False
            #self.marco1.deiconify()
        elif (self.marco2.alturaDATA, self.marco2.anchoDATA, self.marco2.largoDATA) != 0:
            print 'Hola ya ingreso' 
            tkMessageBox.showinfo('Atención', 'Ya ingreso los datos de la caja, si desea corregir los datos presione el botón de RESET')
        else:
            print 'Hola ventana abierta' 
            tkMessageBox.showinfo('Atención', 'Ya se encuentra abierta la ventana, favor de verificar')
        
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
#        elif self.bandera == False:
#            print "Inserte datos"
        if self.num_prueb == 0:
            tkMessageBox.showinfo('Atención', 'Debe realizar la prueba antes de exportar los datos')
        elif self.num_prueb != 0 and self.num_pruebaR: 
            #and path.exists('/home/pi/Desktop/ProgGUI/GUI/resources/graf/GraficoBCT_{}.png'.format(self.num_pruebaR)):
            if self.num_prueb == 1:
                self.docPDF.load_data(largo = self.largoC, ancho = self.anchoC, alto = self.alturaC)
            desp = float(self.xyValue[0])*0.005
            self.xyValue[0] = 0
            self.docPDF.add_PDF(self.segundos, self.xyValue[2], desp)
            self.num_pruebaR = False
            answ=tkMessageBox.askyesno("Atención", "Datos recopilados en PDF, ¿Desea realizar otra pueba?")
            if answ==False:
                self.docPDF.build_PDF()
                tkMessageBox.showinfo('Atención', "Reporte creado con éxito, Se abrirá una ventana donde podrá realizar diferentes acciones con el reporte")
                self.final = VentanaFinal(self.master, self.now, self.docPDF.direc)
                #self.marco1.wait_window(self.final.marco3)
                #if respuesta==True:
                #    commands.getoutput('qpdfview BCT_reporte.pdf')
                self.final.SaveObj(self.resetFile)
                #self.resetFile(False)
            else:
                self.resetFile(False, False)
        else:
            tkMessageBox.showinfo('Atención', 'Debe realizar la prueba antes de exportar los datos')

    def cerrar(self):
        if self.bandera == True:
            self.StopG()
            tkMessageBox.showerror("Atención","Se detuvo la prueba por seguridad")
        respuesta=tkMessageBox.askyesno("Cuidado", "¿Quiere salir del programa?")
        if respuesta==True:
            #sys.exit()
            self.resetFile(False)
            #GPIO.cleanup()
            self.marco1.quit()
        
    def animate(self,i):
        if self.bandera == True:
            # PRIMERO OBTENEMOS EL VALOR
            self.xyValue = self.fW.EscribeArch(False)
            pullData = open("/home/pi/Desktop/ProgGUI/GUI/resources/sampleText.txt","r").read()
            dataList = pullData.split('\n')
            self.xList = []
            self.yList = []
            for eachLine in dataList:
                if len(eachLine) > 1:
                    x, y = eachLine.split(',')
                    self.xList.append(float(x))
                    self.yList.append(float(y))
            self.a.clear()
            print(str(self.xyValue) + " Animate")
            self.a.plot(self.xList, self.yList)
            self.a.set_ylabel("BCT (kg)")
            self.a.set_xlabel('Desplazamiento (mm)')
            self.tempor += 1
            self.esctxtCB()
        else:
            self.a.clear()
            self.a.set_ylabel("BCT (kg)")
            self.a.set_xlabel('Desplazamiento (mm)')
            
    def resetFile(self, edo = True, borra = True):
        if edo == True:
            if self.num_prueb == 0 and self.gg == True:
                tkMessageBox.showinfo('Atención', 'El dispositivo se encuentra en su estado inicial')
            else:
                respuesta=tkMessageBox.askyesno("Cuidado", "¿Desea reiniciar la prueba actual?, se eliminarán los datos obtenidos")
                if respuesta==True:
                    self.ani.event_source.start()
                    self.xyValue = self.fW.EscribeArch(True)
                    print(str(self.xyValue) + " resetFile1")
                    self.esctxtCB()
                    self.bandera = False
                    self.StopG()
                    self.num_prueb = 0
                    self.gg = True
                    self.docPDF.reset_num(self.now)
#            self.ventanaDATA()
        else:
            self.ani.event_source.start()
            self.xyValue = self.fW.EscribeArch(True)
            #print(str(self.xyValue) + " resetFile0")
            self.esctxtCB()
            self.bandera = False
            if borra == (not False):
                self.num_prueb = 0
                self.gg = True
                self.now = datetime.now()
                self.docPDF.reset_num(self.now)
                self.banderaDATA = False
                try:
                    comando = 'mv /home/pi/Desktop/ProgGUI/GUI/resources/graf/*.png /home/pi/Desktop/ProgGUI/GUI/resources/graf/old'
                    commands.getoutput(comando)
                except:
                    print 'Imagenes ya eliminadas'
            print(str(self.xyValue) + " resetFile0 ") + str(borra)
        self.ventanaDATA()
                
                
    def StartG(self):
        if self.banderaDATA == True:
            self.alturaC = self.marco2.alturaDATA
            self.anchoC = self.marco2.anchoDATA
            self.largoC = self.marco2.largoDATA
            self.InfoCj = self.marco2.Datos
            self.num_prueb += 1
            print self.alturaC, self.anchoC, self.largoC
            respuesta=tkMessageBox.askyesno("Cuidado", 
            "¿Está seguro de iniciar la prueba, con los siguientes datos?: \n {}cm de alto, {}cm de ancho, {}cm de largo".format(self.alturaC, self.anchoC, self.largoC))
            if respuesta==True:
                self.num_pruebaR = True
                print "Second number state " + str(self.num_pruebaR)
                #GPIO.output(7, 1)
                self.instanteInicial = datetime.now()
                if self.bandera == False:
                    self.ani.event_source.start() #INICIA/REANUDA ANIMACIÓN
                    self.bandera = True
            else:
                self.num_prueb -= 1
        else:
            tkMessageBox.showerror('Atención', 'Debe ingresar los datos de la caja')
        print 'Numero de pruebas en ventana main ' + str(self.num_prueb)
        
    def StopG(self):
        if self.bandera == True:
            self.ani.event_source.stop() #DETIENE ANIMACIÓN
            self.instanteFinal = datetime.now()
            tiempo = self.instanteFinal - self.instanteInicial 
            self.segundos = tiempo.seconds
            self.bandera = False
        plt.ioff()
        #GPIO.output(7, 0)
        figs = plt.figure(figsize=(7, 3.9), dpi=100)
        pltAr = figs.add_subplot(111)
        try:
            pltAr.plot(self.xList, self.yList)
        except Exception:
            print 'error'
        plt.xlabel('Desplazamiento (mm)')
        plt.ylabel("BCT (kg)")
        plt.savefig('/home/pi/Desktop/ProgGUI/GUI/resources/graf/GraficoBCT_{}.png'.format(self.num_prueb),
                    dpi = 80,
                    transparent = True)
        print("Grafico creado")
        plt.clf()
        
            
    def esctxtCB(self):
        self.txtBCT.delete(0.0, END)
        self.txtBCT.insert(0.0, self.xyValue[1])
        self.txtPos.delete(0.0, END)
        self.txtPos.insert(0.0, self.xyValue[0])