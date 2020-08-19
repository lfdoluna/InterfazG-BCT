# -*- coding: utf-8 -*-
"""
Created on Tue Dec 03 17:48:36 2019
Comentarios: Clase que implementa el manejo de un motor a pasos
Archivo: MotorPAP.py
Version: 0.1
@author: LuisFer
"""

import RPi.GPIO as GPIO
import time
import tkMessageBox

class MotorPAP:
    def __init__(self):
        #GPIO.setmode(GPIO.BOARD)
        self.control_pins = [7,11,13,15]
        for pin in self.control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        self.halfstep_seq1 = [[1,0,0,0],
                              [1,1,0,0],
                              [0,1,0,0],
                              [0,1,1,0],
                              [0,0,1,0],
                              [0,0,1,1],
                              [0,0,0,1],
                              [1,0,0,1]]
        self.halfstep_seq2 = [[1,0,0,1],
                              [0,0,0,1],
                              [0,0,1,1],
                              [0,0,1,0],
                              [0,1,1,0],
                              [0,1,0,0],
                              [1,1,0,0],
                              [1,0,0,0],
                              [0,0,0,0]]
        
    def PasosIzq(self, delay = 0.001):
        #for i in range(512):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.control_pins[pin], self.halfstep_seq1[halfstep][pin])
                    time.sleep(delay)
    
    def PasosDer(self,delay = 0.001):
        #for i in range(512):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.control_pins[pin], self.halfstep_seq2[halfstep][pin])
                    time.sleep(delay)
    def apaga(self):
        for i in range(4):
            GPIO.output(self.control_pins[i], self.halfstep_seq2[8][i])
            time.sleep(0.001)
        
    def limpia(self):
        GPIO.cleanup()