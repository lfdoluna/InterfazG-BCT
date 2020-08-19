#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:52:46 2019
Comentario: Archivo para la escritura y limpieza del archivo sampleText.txt
funcion y = x*math.cos(sqrt(x)30)
@author: pi
"""

import os
import math
import serial
import re

class wFileSer:
    def __init__(self):
        self.i = 0
        self.hValue = 0
        self.lecB  = serial.Serial(port = '/dev/ttyUSB0', 
                                  baudrate = 9600, 
                                  parity = serial.PARITY_NONE, 
                                  stopbits = serial.STOPBITS_ONE, 
                                  bytesize = serial.EIGHTBITS, 
                                  timeout = 1)
        
    def EscribeArch(self, j = False): 
        self. peso = str(self.lecB.readline())
        self. peso = float(re.sub("[^0123456789\.]", "", self. peso))
        if j == True:
            file1 = open("sampleText.txt","w")
            self.i = 0
            self.peso = 0
            file1.write(str(self.i) + "," + str(self.peso) + os.linesep)
            j = False
        else:
            file = open("sampleText.txt","a")
            file.write(str(self.i) + "," + str(self.peso) + os.linesep)
            self.i+= 0.1
        self.leeDevH()
        return [str(round(self.i,4)), str(self.peso), str(self.hValue)]
    
    def leeDevH(self):
        pullData = open("sampleText.txt","r").read()
        dataList = pullData.split('\n')
        self.xList = []
        self.yList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                self.xList.append(float(x))
                self.yList.append(float(y))
                if float(y) > self.hValue:
                    self.hValue = round(float(y), 4)
