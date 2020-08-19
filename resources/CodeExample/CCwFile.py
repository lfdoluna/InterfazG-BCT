#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:52:46 2019
Comentario: Archivo para la escritura y limpieza del archivo sampleText.txt
funcion y = x*math.cos(sqrt(x)30)
@author: pi
"""

import os
import time
from hx711 import HX711

referenceUnit = -2544.7714
hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()
print("Tare done! Add weight now...")

class CCwFile:
    def __init__(self):
        self.lec = 0
        self.i = 0
        self.hValue = 0
        
    def EscribeArch(self, j = False): 
        self.lec = hx.get_weight(5)/1000
        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
        print self.lec
        if j == True:
            file1 = open("sampleText.txt","w")
            self.i = 0
            self.lec = 0
            self.hValue = 0
            file1.write(str(self.i) + "," + str(self.lec) + os.linesep)
            j = False
        else:
            file = open("sampleText.txt","a")
            file.write(str(self.i) + "," + str(self.lec) + os.linesep)
            self.i+= 0.1
        self.leeDevH()
        return [str(round(self.i,4)), str(round(self.lec,4)), str(self.hValue)]
    
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