#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:04:43 2020

@author: pi
"""
from Tkinter import PhotoImage,\
                    Label,\
                    Button,\
                    Text,\
                    END,\
                    Toplevel,\
                    Radiobutton,\
                    IntVar,\
                    StringVar#,\
#                    Tk
from ttk import Combobox
from PSQLmerma import PSQLmerma as PSQLmerma1
import ttk as TTK
import tkMessageBox
#import sys
# from tkinter import re

class DATAin:
    def __init__(self, maestro):
        # Atributo de conteo'''
        self.botonClics = 0
        self.bandDATA = 3
        self.operacion=""
        self.alturaDATA = 0
        self.anchoDATA = 0
        self.largoDATA = 0
        self.Datos = []
        for i in range (7):
            self.Datos.append('')
            
        self.consoleSQL = PSQLmerma1()
        #gg = Tkk.Notebook(maestro)
        self.top = Toplevel(maestro)
        self.top.title('Introduce medidas de la caja')
        self.top.update_idletasks()
#        w = self.top.winfo_screenwidth()
#        h = self.top.winfo_screenheight()
#        size = tuple(int(_) for _ in self.top.geometry().split('+')[0].split('x'))
#        x = w/2 - size[0]/2
#        y = h/2 - size[1]/2
#        print size + (x, y)
#        
        self.top.geometry("+150+60")
        #self.top.iconbitmap('/home/pi/Desktop/ProgGUI/GUI/resources/ICO/IconoBCT.ico')
        
        #MARCO3 ESEL LINEZO DONDE SE DIBUJAN LAS PESTAÑAS
        self.marco3 = TTK.Notebook(self.top)

        # CREAMOS EL MARCO PARA CADA UNA DE LAS PESTAÑAS
        self.page1 = TTK.Frame(self.marco3)
        self.page2 = TTK.Frame(self.marco3)
        self.page3 = TTK.Frame(self.marco3)
        self.page4 = TTK.Frame(self.marco3)
        self.page5 = TTK.Frame(self.marco3)
       
        # AGREGAMOS EL MARCO A LAS PESTAÑAS Y SU NOMBRE
        self.marco3.add(self.page1, text='Dimensiones de la caja')
        self.marco3.add(self.page2, text='Descripción de la caja')
        self.marco3.add(self.page3, text='Descripción de la prueba')
        self.marco3.add(self.page4, text='Datos del cliente')
        self.marco3.add(self.page5, text='Resumen de datos')
        self.marco3.grid()
        
        # AGREGAGOS CONTENIDO A PESTAÑA 1
        self.IMGcaja = PhotoImage(file = '/home/pi/Desktop/ProgGUI/GUI/resources/img/cajaDATA/caja.png')
        self.IMGancho= PhotoImage(file = '/home/pi/Desktop/ProgGUI/GUI/resources/img/cajaDATA/anchoSelect.png')
        self.IMGlargo= PhotoImage(file = '/home/pi/Desktop/ProgGUI/GUI/resources/img/cajaDATA/largoSelect.png')
        self.IMGalto = PhotoImage(file = '/home/pi/Desktop/ProgGUI/GUI/resources/img/cajaDATA/altoSelect.png')
        
        self.cajaLB = Label(self.page1, image = self.IMGcaja)
        self.cajaLB.grid(row = 0, column = 4, rowspan = 5, columnspan = 3)
        
        self.txtLB = 'Seleccione un botón e ingrese \n las medidas en cm'
        self.LB = Label(self.page1, font =('Helvetica', 15), text = self.txtLB)
        self.LB.grid(row = 0, column = 0, columnspan = 4)
        
        self.CBdata = Text(self.page1, state="disabled", width=40, height=2, font=("Helvetica",15))
        self.CBdata.grid(row = 1, column = 0, columnspan = 4)
        
        self.anchoL = Label(self.page1, 
                            font =('Helvetica', 15), 
                            text = "")
        self.anchoL.grid(row =4, column = 4, sticky = 's')
        self.BTNancho = Button(self.page1, width=5, height=1, font=("Helvetica",15), text = 'Ancho', command =lambda: self.selectCB('an'))
        self.BTNancho.grid(row = 5, column = 4)
        self.largoL = Label(self.page1, 
                            font =('Helvetica', 15), 
                            text = "")
        self.largoL.grid(row =4, column = 5, sticky = 's')
        self.BTNlargo = Button(self.page1, width=5, height=1, font=("Helvetica",15), text = 'Largo', command =lambda: self.selectCB('la'))
        self.BTNlargo.grid(row = 5, column = 5)
        self.altoL  = Label(self.page1, 
                            font =('Helvetica', 15), 
                            text = "")
        self.altoL.grid(row =4, column = 6, sticky = 's')
        self.BTNalto = Button(self.page1, width=5, height=1, font=("Helvetica",15), text = 'Alto', command =lambda: self.selectCB('al'))
        self.BTNalto.grid(row = 5, column = 6)
        
        boton1 = self.crearBoton(1)
        boton2 = self.crearBoton(2)
        boton3 = self.crearBoton(3)
        boton4 = self.crearBoton(4)
        boton5 = self.crearBoton(5)
        boton6 = self.crearBoton(6)
        boton7 = self.crearBoton(7)
        boton8 = self.crearBoton(8)
        boton9 = self.crearBoton(9)
        boton0 = self.crearBoton(0,ancho=7)
        botonErase = self.crearBoton(u"\u232B",escribir=False)
        botonErase['background'] = "red"
        botonErase.grid(row = 2, column = 3)
        botonEnter = self.crearBoton(u"\u21B5",escribir=False)
        botonEnter['background'] = "green"
        botonEnter.grid(row = 3, column = 3)
        botondot = self.crearBoton('.')
        
        #Ubicación de los botones
        botones=[boton7, boton8, boton9,
                 boton4, boton5, boton6,
                 boton1, boton2, boton3,
                 boton0]
        contador=0
        for fila in range(2,5):
            for columna in range(3):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        #Ubicar el último botón al final
        botones[contador].grid(row=5,column=0,columnspan=2)
        botondot.grid(row = 5, column = 2)
        
        # AGREGAGOS CONTENIDO A PESTAÑA 2
        Label(self.page2, 
              font =('Helvetica', 15), 
              text = 'Seleccione:')\
              .grid(row = 0, column = 0,columnspan = 5)
              
        Label(self.page2, 
              font =('Helvetica', 15), 
              text = 'Estilo de caja')\
              .grid(row = 1, column = 0)
              
        self.listCaja = Combobox(self.page2,
                                 state="readonly",
                                 values = ["Caja troquelada", "Caja est" + u"\xe1" + "ndar"],
                                 font =('Helvetica', 15))
        self.listCaja.grid(row = 2, column = 0)
        Label(self.page2, 
              font =('Helvetica', 15), 
              text = '             ')\
              .grid(row = 2, column = 1)
        
        Label(self.page2, 
              font =('Helvetica', 15), 
              text = 'Tipo de flauta')\
              .grid(row = 1, column = 2)
        self.listFlauta = Combobox(self.page2,
                                   state="readonly",
                                   values = ["Corrugado sencillo B", "Corrugado sencillo C", "Corrugado sencillo E", "Doble corrugado BC", "Doble corrugado EB"],
                                   font =('Helvetica', 15))
        self.listFlauta.grid(row = 2, column = 2)
        Label(self.page2, 
              font =('Helvetica', 15), 
              text = '             ')\
              .grid(row = 2, column = 3)
              
              
        Label(self.page2, 
              font =('Helvetica', 15), 
              text = 'Dirección de la flauta')\
              .grid(row = 1, column = 4)
        self.listFlautaD= Combobox(self.page2,
                                   state="readonly",
                                   values = ["Horizontal", "Vertical"],
                                   font =('Helvetica', 15))
        self.listFlautaD.grid(row = 2, column = 4)
                                   
        Label(self.page2, 
              font =('Helvetica', 15), 
              text = '             ')\
              .grid(row = 3, column = 0, columnspan = 3)
        
        Label(self.page2, 
              font =('Helvetica', 15), 
              text = 'Grado del material')\
              .grid(row = 4, column = 0)
        self.listGradoM= Combobox(self.page2,
                                   state="readonly",
                                   values = ["No aplica", "20 ECT", "21 ECT", "23 ECT", "26 ECT", "29 ECT", "32 ECT", "44 ECT", "48 ECT", "50 ECT", "61 ECT", "71 ECT"],
                                   font =('Helvetica', 15))
        self.listGradoM.grid(row = 5, column = 0)
                                   
        Label(self.page2, 
              font =('Helvetica', 15), 
              text = 'Tipo de unión')\
              .grid(row = 4, column = 2)
        self.listUnion= Combobox(self.page2,
                                   state="readonly",
                                   values = ["Pegado", "Grapado", "Armado automático"],
                                   font =('Helvetica', 15))
        self.listUnion.grid(row = 5, column = 2)
        
        # AGREGAMOS CONTEIDO A PAGE3
        Label(self.page3, 
              font =('Helvetica', 15), 
              text = 'Método de cierre')\
              .grid(row = 0, column = 0)
        self.listCierre= Combobox(self.page3,
                                   state="readonly",
                                   values = ["Conforme a la TAPPI T 804", "Otro", "No aplica"],
                                   font =('Helvetica', 15))
        self.listCierre.grid(row = 1, column = 0)
                                   
        Label(self.page3, 
              font =('Helvetica', 15), 
              text = '             ')\
              .grid(row = 0, column = 1)
              
        Label(self.page3, 
              font =('Helvetica', 15), 
              text = 'Orientación de la prueba')\
              .grid(row = 0, column = 2)
        self.listOrientaC= Combobox(self.page3,
                                   state="readonly",
                                   values = ["Arriba a abajo", "Extremo a extremo", "Lado a lado"],
                                   font =('Helvetica', 15))
        self.listOrientaC.grid(row = 1, column = 2)
        
        # AGREGAMOS CONTENIDO A PAGE 4
        self.txtLB = 'Ingresar datos o buscar por número de pedido'
        self.state = TTK.Label(self.page4, font =('Helvetica', 15), text = self.txtLB)
        self.state.grid(row = 0, column = 0, columnspan = 12)
        
        boton1 = self.crearBotonP4(1)
        boton2 = self.crearBotonP4(2)
        boton3 = self.crearBotonP4(3)
        boton4 = self.crearBotonP4(4)
        boton5 = self.crearBotonP4(5)
        boton6 = self.crearBotonP4(6)
        boton7 = self.crearBotonP4(7)
        boton8 = self.crearBotonP4(8)
        boton9 = self.crearBotonP4(9)
        boton0 = self.crearBotonP4(0)
        
        botonQ = self.crearBotonP4('Q')
        botonW = self.crearBotonP4('W')
        botonE = self.crearBotonP4('E')
        botonR = self.crearBotonP4('R')
        botonT = self.crearBotonP4('T')
        botonY = self.crearBotonP4('Y')
        botonU = self.crearBotonP4('U')
        botonI = self.crearBotonP4('I')
        botonO = self.crearBotonP4('O')
        botonP = self.crearBotonP4('P')
        botonA = self.crearBotonP4('A')
        botonS = self.crearBotonP4('S')
        botonD = self.crearBotonP4('D')
        botonF = self.crearBotonP4('F')
        botonG = self.crearBotonP4('G')
        botonH = self.crearBotonP4('H')
        botonJ = self.crearBotonP4('J')
        botonK = self.crearBotonP4('K')
        botonL = self.crearBotonP4('L')
        botonNN= self.crearBotonP4('Ñ')
        botonZ = self.crearBotonP4('Z')
        botonX = self.crearBotonP4('X')
        botonC = self.crearBotonP4('C')
        botonV = self.crearBotonP4('V')
        botonB = self.crearBotonP4('B')
        botonN = self.crearBotonP4('N')
        botonM = self.crearBotonP4('M')
        botondot = self.crearBotonP4('.')
        botonguion = self.crearBotonP4('-')
        botonguionb = self.crearBotonP4(',')
        botonErase = self.crearBotonP4(u"\u232B",escribir=False)
        botonErase['background'] = "red"
        botonErase.grid(row = 3, column = 11)
        botonEnter = self.crearBotonP4(u"\u21B5",escribir=False,alto=2)
        botonEnter['background'] = "green"
        botonEnter.grid(row = 1, column = 11, rowspan = 2, sticky = 's')
        botonSpace = Button(self.page4, text=u"\u2423", width=5, height=1, font=("Helvetica",15), command=lambda:self.clickP4(' ',True))
        botonSpace.grid(row = 4, column = 11)
        
        #Ubicación de los botones
        botones= [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton0,
                  botonQ, botonW, botonE, botonR, botonT, botonY, botonU, botonI, botonO, botonP, 
                  botonA, botonS, botonD, botonF, botonG, botonH, botonJ, botonK, botonL, botonNN, 
                  botonZ, botonX, botonC, botonV, botonB, botonN, botonM, botondot, botonguion, botonguionb]
        contador=0
        for fila in range(1,5):
            for columna in range(10):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        
        self.ChkSe = IntVar()
        self.RBCliente = Radiobutton(self.page4, text = 'Cliente',font =('Helvetica', 15), variable = self.ChkSe, value = 1)
        self.RBCliente.grid(row = 5, column = 2, columnspan = 2, sticky = 'w')
        
        self.RBProducto = Radiobutton(self.page4, text = 'Producto',font =('Helvetica', 15), variable = self.ChkSe, value = 2)
        self.RBProducto.grid(row = 5, column = 4, columnspan = 2, sticky = 'w')
        
        self.RBBuscar = Radiobutton(self.page4, text = 'Buscar por pedido',font =('Helvetica', 15), variable = self.ChkSe, value = 3)
        self.RBBuscar.grid(row = 5, column = 6, columnspan = 3, sticky = 'w')
        
        self.CBdata2 = Text(self.page4, state="disabled", width=40, height=1, font=("Helvetica",15))
        self.CBdata2.grid(row = 6, column = 0, columnspan = 12)
                
        self.clienteL = TTK.Label(self.page4, font =('Helvetica', 15), text = 'Cliente:')
        self.clienteL.grid(row = 7, column = 0, columnspan = 11, sticky = 'w')
        
        self.ProductoL = TTK.Label(self.page4, font =('Helvetica', 15), text = 'Producto:')
        self.ProductoL.grid(row = 8, column = 0, columnspan = 11, sticky = 'w')
        
        # AGREGAMOS CONTENIDO A PAGE 5
        Label(self.page5, 
              font =('Helvetica', 15), 
              text = '*                                                                                                                                                *').grid(row = 0,
#              text = '123456789_123456789_123456789_123465789_123456789_123456789_123456789_123456789_12',
              #text = '____________________________').grid(row = 0,
                                                                     column = 0,
                                                                     columnspan = 3)
        Label(self.page5, 
              font =('Helvetica', 15),
              text = '_________________________________________').grid(row = 0,
                                                                     column = 0,)
        
        Label(self.page5, 
              font =('Helvetica', 15),
              text = '_________________________________________').grid(row = 0,
                                                                     column = 1)
#        Label(self.page5, 
#              font =('Helvetica', 15),
#              text = '___________________________').grid(row = 0,
#                                                                     column = 2)
        Label(self.page5, 
              font =('Helvetica', 15), 
              text = 'Verifique los datos ingresado:').grid(row = 0,
                                                                     column = 0,
                                                                     columnspan = 2)
        self.StxtCliente = StringVar(value = '*')
        self.txtCliente = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Cliente:')
        self.txtCliente.grid(row = 1, column = 0, sticky = 'w')
        self.txtClienteL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtCliente)
        self.txtClienteL.place(x = 79, y = 28)
        
        self.StxtProducto = StringVar(value = '*')
        self.txtProducto = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Producto: ')
        self.txtProducto.grid(row = 2, column = 0, columnspan = 2, sticky = "w")
        self.txtProductoL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtProducto)
        self.txtProductoL.place(x = 99, y = 56)
        
        self.StxtLargo = StringVar(value = '*')
        self.txtLargo = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Largo:')
        self.txtLargo.grid(row = 3, column = 0, sticky = "w")
        self.txtLargoL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtLargo)
        self.txtLargoL.place(x= 69, y = 84)
        
        self.StxtAlto = StringVar(value = '*')
        self.txtAlto = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Alto:')
        self.txtAlto.place(x = 310, y = 84)
        self.txtAltoL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtAlto)
        self.txtAltoL.place(x = 363, y = 84)
        
        self.StxtAncho = StringVar(value = '*')
        self.txtAncho = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Ancho: ')
        self.txtAncho.place(x= 590, y = 84)
        self.txtAnchoL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtAncho)
        self.txtAnchoL.place(x= 666, y = 84)
        
        self.StxtStlCj = StringVar(value = '*')
        self.txtStlCj = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Estilo caja:')
        self.txtStlCj.grid(row = 4, column = 0, sticky = "w")
        self.txtStlCjL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtStlCj)
        self.txtStlCjL.place(x= 110, y = 112)
        
        self.StxtTpFlt = StringVar(value = '*')
        self.txtTpFlt = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Tipo de flauta:')
        self.txtTpFlt.grid(row = 4, column = 1, sticky = "w")
        self.txtTpFltL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtTpFlt)
        self.txtTpFltL.place(x= 594, y = 112)
        
        self.StxtDrccnFlt = StringVar(value = '*')
        self.txtDrccnFlt = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Dirección de la flauta: ')
        self.txtDrccnFlt.grid(row = 5, column = 0, sticky = "w")
        self.txtDrccnFltL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtDrccnFlt)
        self.txtDrccnFltL.place(x= 216, y = 140)
        
        self.StxtGrdMtrl = StringVar(value = '*')
        self.txtGrdMtrl = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Grado del material: ')
        self.txtGrdMtrl.grid(row = 5, column = 1, sticky = "w")
        self.txtGrdMtrlL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtGrdMtrl)
        self.txtGrdMtrlL.place(x= 640, y = 140)
        
        
        self.StxtTpUnn = StringVar(value = '*')
        self.txtTpUnn = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Tipo de unión: ')
        self.txtTpUnn.grid(row = 6, column = 0, sticky = "w")
        self.txtTpUnnL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtTpUnn)
        self.txtTpUnnL.place(x= 138, y = 168)
        
        self.StxtMtdCrr = StringVar(value = '*')
        self.txtMtdCrr = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Método de cierre: ')
        self.txtMtdCrr.grid(row = 6, column = 1, sticky = "w")
        self.txtMtdCrrL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtMtdCrr)
        self.txtMtdCrrL.place(x= 623, y = 168)
        
        self.StxtOrntcn = StringVar(value = '*')
        self.txtOrntcn = Label(self.page5, font = ('Helvetica', 15, 'italic'), text = '*Orientación de la prueba: ')
        self.txtOrntcn.grid(row = 7, column = 0, sticky = "w")
        self.txtOrntcnL = Label(self.page5, font = ('Helvetica', 15), textvariable = self.StxtOrntcn)
        self.txtOrntcnL.place(x= 243, y = 197)
        
        cc = Button(self.page5, font = ('Helvetica', 15, "bold"), text = 'Cerrar', bg = "red", command = self.cerrarB)#.place(x = 20, y = 20)
        cc.grid(row = 8, column = 0, columnspan = 2)
        
        # OBTENER LO QUE CONTIENEN CADA LISTA
        self.listCaja.bind("<<ComboboxSelected>>", self.getList)
        self.listCierre.bind("<<ComboboxSelected>>", self.getList)
        self.listFlauta.bind("<<ComboboxSelected>>", self.getList)
        self.listFlautaD.bind("<<ComboboxSelected>>", self.getList)
        self.listGradoM.bind("<<ComboboxSelected>>", self.getList)
        self.listOrientaC.bind("<<ComboboxSelected>>", self.getList)
        self.listUnion.bind("<<ComboboxSelected>>", self.getList)
        
        self.top.protocol("WM_DELETE_WINDOW", self.cerrar)
        
    def motion(self, event):
        self.posy.set(event.y)
        self.posx.set(event.x)
        
    def selectCB(self,selecc):
        if selecc == 'al':
            self.LB['text'] = 'Usted selecciono alto'
            self.cajaLB['image'] = self.IMGalto
            self.bandDATA = 0
        elif selecc == 'an':
            self.LB['text'] = 'Usted selecciono ancho'
            self.cajaLB['image'] = self.IMGancho
            self.bandDATA = 1
        elif selecc == 'la':
            self.LB['text'] = 'Usted selecciono largo'
            self.cajaLB['image'] = self.IMGlargo
            self.bandDATA = 2
        
    def crearBoton(self, valor, escribir=True, ancho=5, alto=1):
        return Button(self.page1, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))
        
    def crearBotonP4(self, valor, escribir=True, ancho=5, alto=1):
        return Button(self.page4, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.clickP4(valor,escribir))
        
    def conteo(self):
        self.botonClics += 1
        self.btnCLK['text'] = 'Clics totales = ' + str(self.botonClics)
        
        
    def click(self, texto, escribir):
        if not escribir:
            if texto==u"\u21B5" and self.operacion!="" and self.bandDATA != 3:
                if self.bandDATA == 0:
                    try:
                        self.alturaDATA = float(self.operacion)
                        self.LB['text'] = 'Usted ingreso ' + str(self.alturaDATA) + 'cm en altura'
                        self.altoL['text'] = str(self.alturaDATA) + 'cm'
                        self.StxtAlto.set(str(self.alturaDATA) + 'cm')
                        self.changeTXT(self.StxtAlto, str(self.alturaDATA) + 'cm', self.txtAlto, 'Alto:')
                    except ValueError:
                        self.LB['text'] = 'Atención \n El dato ingresado no es un número válido,\n favor de verificar'
                        
                elif self.bandDATA == 1:
                    try:
                        self.anchoDATA = float(self.operacion)
                        self.LB['text'] = 'Usted ingreso ' + str(self.anchoDATA) + 'cm en ancho'
                        self.changeTXT(self.StxtAncho, str(self.anchoDATA) + 'cm', self.txtAncho, 'Ancho:')
                        self.anchoL['text'] = str(self.anchoDATA) + 'cm'
                    except ValueError:
                        self.LB['text'] = 'Atención \n El dato ingresado no es un número válido,\n favor de verificar'
                elif self.bandDATA == 2:
                    try:
                        self.largoDATA = float(self.operacion)
                        self.LB['text'] = 'Usted ingreso ' + str(self.largoDATA ) + 'cm en largo'
                        self.changeTXT(self.StxtLargo, str(self.largoDATA ) + 'cm', self.txtLargo, 'Largo:')
                        self.largoL['text'] = str(self.largoDATA ) + 'cm'
                    except ValueError:
                        self.LB['text'] = 'Atención \n El dato ingresado no es un número válido,\n favor de verificar'
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
    
    def clickP4(self, texto, escribir):
        self.ChkSel = int(self.ChkSe.get())
        print self.ChkSel
        if not escribir:
            if texto==u"\u21B5" and self.operacion!="" and self.ChkSel != 0:
                print 'gg'
                if self.ChkSel == 1:
                    self.cliente = self.operacion
                    self.clienteL['text'] = 'Cliente: ' + str(self.cliente)
                    self.changeTXT(self.StxtCliente, str(self.cliente), self.txtCliente, 'Cliente:')
                elif self.ChkSel == 2:
                    self.Producto = self.operacion
                    self.ProductoL['text'] = 'Producto: ' + str(self.Producto)
                    self.changeTXT(self.StxtProducto, str(self.Producto), self.txtProducto, 'Producto:')
                elif self.ChkSel == 3:
                    self.top.iconify()
                    self.consoleSQL.consulta('pedido', str(self.operacion))
                    try:
                        self.cliente = self.consoleSQL.cliente
                        self.clienteL['text'] = 'Cliente: ' + str(self.cliente)
                        self.changeTXT(self.StxtCliente, str(self.cliente), self.txtCliente, 'Cliente:')
                        self.Producto = self.consoleSQL.producto
                        self.ProductoL['text'] = 'Producto: ' + str(self.Producto)
                        self.changeTXT(self.StxtProducto, str(self.Producto), self.txtProducto, 'Producto:')
                    except:
                        tkMessageBox.showerror('Atención','No se encontró el pedido favor de verificar')
                self.operacion = ''
                self.limpiarPantalla(2)
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla(2)
            elif self.ChkSel == 0:
                self.top.iconify()
                tkMessageBox.showerror("Atención", 'Debe seleccionar una opción')
        #Mostrar texto
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto, 2)
        self.top.deiconify()
        return
    
    def changeTXT(self, StringVarTXT, setStr, LabelTXT, txtLabel):
        StringVarTXT.set(setStr)
        LabelTXT['text'] = txtLabel
        LabelTXT['font'] = ('Helvetica', 15, "bold")
        
    def limpiarPantalla(self, cb = 1):
        if cb ==2:
            self.CBdata2.configure(state="normal")
            self.CBdata2.delete("1.0", END)
            self.CBdata2.configure(state="disabled")
        else:
            self.CBdata.configure(state="normal")
            self.CBdata.delete("1.0", END)
            self.CBdata.configure(state="disabled")
        return
    

    def mostrarEnPantalla(self, valor, cb = 1):
        if cb == 2:
            self.CBdata2.configure(state="normal")
            self.CBdata2.insert(END, valor)
            self.CBdata2.configure(state="disabled")
        else:
            self.CBdata.configure(state="normal")
            self.CBdata.insert(END, valor)
            self.CBdata.configure(state="disabled")
        return
    
    def getList(self, event):
        self.CheckList(self.listCaja, 0, self.StxtStlCj, 'Estilo caja: ', self.txtStlCj)
        self.CheckList(self.listFlauta, 1, self.StxtTpFlt, 'Tipo de flauta: ', self.txtTpFlt)
        self.CheckList(self.listFlautaD, 2, self.StxtDrccnFlt, 'Dirección de  la flauta: ', self.txtDrccnFlt)
        self.CheckList(self.listGradoM, 3, self.StxtGrdMtrl, 'Grado del material: ', self.txtGrdMtrl)
        self.CheckList(self.listUnion, 4, self.StxtTpUnn, 'Tipo de unión: ', self.txtTpUnn)
        self.CheckList(self.listCierre, 5, self.StxtMtdCrr, 'Método de cierre: ', self.txtMtdCrr)
        self.CheckList(self.listOrientaC, 6, self.StxtOrntcn, 'Orientación de la prueba: ', self.txtOrntcn)
        #hola
        
    def CheckList(self, lista, num_list, StrVarL, txt, labelTXT,):
        gg = lista.get()
        print gg
        if gg != '':
            self.Datos[num_list] = lista.get()
            if num_list == 0:
                if self.Datos[0] == (u'Caja est\xe1ndar'):
                    self.Datos[0] = str('Caja estándar')
            elif num_list == 4:
                if self.Datos[4] == (u'Armado autom\xe1tico'):
                    self.Datos[4] = ('Armado automático')
            StrVarL.set(self.Datos[num_list])
            labelTXT['text'] = txt
            labelTXT['font'] = ('Helvetica', 15, "bold")
            
        
    def cerrar(self):
        self.top.iconify()
        tkMessageBox.showinfo("Atención", "Si desea salir, debe hacerlo desde el botón ubicado en la pestaña de Resumen de datos.")
        self.top.deiconify()
        
    def cerrarB(self):
        self.top.iconify()
        respuesta=tkMessageBox.askyesno("Atención", "Usted esta a punto de salir, ¿Los datos ingresados son los correctos?")
        if respuesta==True:
            self.top.destroy()
        try:
            self.top.deiconify()
        except:
            print "Ventana cerrada"
            
#ventana = Tk()
#final = DATAin(ventana)
#ventana.mainloop()