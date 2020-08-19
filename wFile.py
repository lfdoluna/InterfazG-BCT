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

class wFile:
    def __init__(self):
        self.lec = 0
        self.i = 0
        self.hValue = 0
        
    def EscribeArch(self, j = False):
        self.lec = math.fabs(0.5*self.i*math.cos(math.sqrt(100*self.i)))
        if j == True:
            file1 = open("/home/pi/Desktop/InterfazG-BCT/resources/sampleText.txt","w")
            self.i = 0
            self.lec = 0
            self.hValue = 0
            file1.write(str(self.i) + "," + str(self.lec) + os.linesep)
            j = False
        else:
            file = open("/home/pi/Desktop/InterfazG-BCT/resources/sampleText.txt","a")
            file.write(str(self.i) + "," + str(self.lec) + os.linesep)
            self.i+= 0.1
            if self.lec > self.hValue:
                self.hValue = self.lec
        #self.leeDevH()
        return [str(round(self.i-0.1,4)), str(round(self.lec,4)), str(round(self.hValue,4))]