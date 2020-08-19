#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:51:13 2020
Archivo: VentanaFinal.py
Comentarios: Clase que implementa la apertura  de una ventana en Tkinter python
2.7, crea  una ventana con pestañas  para seleccionar una opción para manipular
el reporte creado por ReportLab
@author: LFLQ
"""
from Tkinter import Button as BT,\
                    Text as tkText,\
                    END as tkEND,\
                    Toplevel as tkToplevel
from tkinter import filedialog
#from datetime import datetime
import tkMessageBox
import ttk as TTK
import commands
from sentmail import *
#from GUI2_BCT import docPDF

class VentanaFinal:
    def __init__(self, maestro, tiempo_ahora, directorio):
        self.carpeta = directorio
        months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        month = months[tiempo_ahora.month - 1]
        self.tiempo = tiempo_ahora.strftime('%H.%M')
        self.fecha = "{}{}{}".format(tiempo_ahora.day, month, tiempo_ahora.year)
        
        self.top2 = tkToplevel(maestro)
        self.top2.title('Seleccione una pestaña')
        self.top2.geometry("+80+60")
        self.top2.protocol("WM_DELETE_WINDOW", self.cerrar)
        #self.top2.iconbitmap('/home/pi/Desktop/ProgGUI/GUI/resources/ICO/IconoBCT.ico')
        
        # Inicialización del objeto para el envio del correo
        self.operacion = ''
        self.mailto = sentmail()
        
        #MARCO3 ESEL LINEZO DONDE SE DIBUJAN LAS PESTAÑAS
        self.marco3 = TTK.Notebook(self.top2)

        # CREAMOS EL MARCO PARA CADA UNA DE LAS PESTAÑAS
        self.page1 = TTK.Frame(self.marco3)
        self.page2 = TTK.Frame(self.marco3)
       
        # AGREGAMOS EL MARCO A LAS PESTAÑAS Y SU NOMBRE
        self.marco3.add(self.page1, text='Enviar por correo electrónico')
        self.marco3.add(self.page2, text='Guardar / Imprimir / Ver PDF')
        self.marco3.grid()
        
        # CONTENIDO DE LA PESTAÑA self.page1
#        self.combo = TTK.Combobox(self.page1, state="readonly", font =('Helvetica'), text = 'Hola', command )
#        self.combo["values"] = ["Python", "C", "C++", "Java"]
#        self.combo.grid(row = 0, column = 0)
        
        self.txtLB = 'Por favor ingrese el correo donde desea recibir el reporte'
        self.state = TTK.Label(self.page1, font =('Helvetica', 15), text = self.txtLB)
        self.state.grid(row = 0, column = 0, columnspan = 11)
        
        botonQ = self.crearBoton('q')
        botonW = self.crearBoton('w')
        botonE = self.crearBoton('e')
        botonR = self.crearBoton('r')
        botonT = self.crearBoton('t')
        botonY = self.crearBoton('y')
        botonU = self.crearBoton('u')
        botonI = self.crearBoton('i')
        botonO = self.crearBoton('o')
        botonP = self.crearBoton('p')
        botonA = self.crearBoton('a')
        botonS = self.crearBoton('s')
        botonD = self.crearBoton('d')
        botonF = self.crearBoton('f')
        botonG = self.crearBoton('g')
        botonH = self.crearBoton('h')
        botonJ = self.crearBoton('j')
        botonK = self.crearBoton('k')
        botonL = self.crearBoton('l')
        botonNN= self.crearBoton('ñ')
        botonZ = self.crearBoton('z')
        botonX = self.crearBoton('x')
        botonC = self.crearBoton('c')
        botonV = self.crearBoton('v')
        botonB = self.crearBoton('b')
        botonN = self.crearBoton('n')
        botonM = self.crearBoton('m')
        botondot = self.crearBoton('.')
        botonguion = self.crearBoton('-')
        botonguionb = self.crearBoton('_')
        botonErase = self.crearBoton(u"\u232B",escribir=False)
        botonErase['background'] = "red"
        botonErase.grid(row = 3, column = 11)
        botonEnter = self.crearBoton(u"\u21B5",escribir=False,alto=2)
        botonEnter['background'] = "green"
        botonEnter.grid(row = 1, column = 11, rowspan = 2, sticky = 's')
        
        #Ubicación de los botones
        botones= [botonQ, botonW, botonE, botonR, botonT, botonY, botonU, botonI, botonO, botonP, 
                  botonA, botonS, botonD, botonF, botonG, botonH, botonJ, botonK, botonL, botonNN, 
                  botonZ, botonX, botonC, botonV, botonB, botonN, botonM, botondot, botonguion, botonguionb]
        contador=0
        for fila in range(1,4):
            for columna in range(10):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
                
        self.CBdata = tkText(self.page1, state="disabled", width=60, height=1, font=("Helvetica",15))
        self.CBdata.grid(row = 4, column = 0, columnspan = 12, sticky = 'w')
                
        archimex = TTK.Label(self.page1, font =('Helvetica', 15), text = '@archimex.com.mx')
        archimex.grid(row = 4, column = 8, columnspan = 4, sticky = 'w')
        
        # CONTENIDO DE LA PESTAÑA self.page2
        self.txtLB2 = 'Seleccione un botón de la acción que desea realizar'
        self.state2 = TTK.Label(self.page2, font =('Helvetica', 15), text = self.txtLB2)
        self.state2.grid(row = 0, column = 0, columnspan = 5)
        
        self.txtLB2 = 'Guardar archivo en\nuna carpeta específica'
        self.save = BT(self.page2, text=self.txtLB2, font=("Helvetica",15), command=self.carpetaselec)
        self.save.grid(row = 1, column = 0)
        
        self.txtLB2 = 'Ver Archivo\nPDF'
        self.view = BT(self.page2, text=self.txtLB2, font=("Helvetica",15), command=self.ver_PDF)
        self.view.grid(row = 1, column = 2)
        
        self.txtLB2 = 'Imprimir\nreporte'
        self.prPDF = BT(self.page2, text=self.txtLB2, font=("Helvetica",15), command=self.imprime)
        self.prPDF.grid(row = 1, column = 4)
        
    def imprime(self):
        self.top2.iconify()
        # CAMBIAR DIRECTORIO
        answ=tkMessageBox.askyesno("Atención", "El archivo se enviará a la impresora ubicada en calidad, ¿Está seguro de continuar?")
        if answ==True:
            #commands.getoutput('lp -d impresora_calidad {}'.format(self.carpeta))
            print 'lp -d impresora_calidad {}'.format(self.carpeta)
        self.top2.deiconify()
        
    def ver_PDF(self):
        self.top2.iconify()
        commands.getoutput('qpdfview {}'.format(self.carpeta))
        self.top2.deiconify()
        
    def carpetaselec(self):
        self.top2.iconify()
        directorio=filedialog.askdirectory()
        #docPDF
        if directorio!="":
            self.state2['text'] = 'Seleccionó el directorio ' + directorio
            comando = 'cp {} {}/BCT_informe_{}_{}.pdf'.format(self.carpeta, directorio, self.fecha, self.tiempo)
            commands.getoutput(comando)
            print(comando)
        self.top2.deiconify()
                
    def crearBoton(self, valor, escribir=True, ancho=5, alto=1):
        return BT(self.page1, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))
        
    #Controla el evento disparado al hacer click en un botón
    def click(self, texto, escribir):
        #Si el parámetro 'escribir' es True, entonces el parámetro texto debe mostrarse en pantalla. Si es False, no.
        if not escribir:
            #Sólo calcular si hay una operación a ser evaluada y si el usuario presionó '='
            if texto==u"\u21B5" and self.operacion!="":
                correo = str(self.operacion) + '@archimex.com.mx'
                self.mailto.destino(correo)
                self.state['text'] = 'Correo ingresado ' + correo
                self.top2.iconify()
                answ=tkMessageBox.askyesno("Atención", "Se ingreso el correo " + correo + ", ¿Es correcto el correo ingresado?")
                if answ==True:
                    self.mailto.sent(self.carpeta)
                    self.top2.deiconify()
                    self.state['text'] = 'Correo enviado correctamente a ' + correo
                print 'Hola desde borrar'
                self.operacion = ''
                self.limpiarPantalla()
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla()
        #Mostrar texto
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)
        return
    
    #Borra el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.CBdata.configure(state="normal")
        self.CBdata.delete("1.0", tkEND)
        self.CBdata.configure(state="disabled")
        return
    

    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def mostrarEnPantalla(self, valor):
        self.CBdata.configure(state="normal")
        self.CBdata.insert(tkEND, valor)
        self.CBdata.configure(state="disabled")
        return
    
    def SaveObj(self, obj):
        self.obj = obj
        
    def cerrar(self):
        self.top2.iconify()
        respuesta=tkMessageBox.askyesno("Precaución", "Usted esta a punto de salir, ¿Desea realizar otra prueba de BCT?. Si selecciona No, se cerrará la ventana")
        if respuesta==True:
            self.obj(False)
            self.top2.destroy()
        else:
            self.top2.quit()
        try:
            self.top2.deiconify()
        except:
            print "Ventana cerrada"
        
#ventana = TK()
#final = VentanaFinal(ventana)
#ventana.mainloop()