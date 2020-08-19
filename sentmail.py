#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 10:59:24 2020
Archivo: sentmail.py
Comentario: Clase sentmail, que se  encarga de  realizar el  envío del  reporte
    que genera la maquina de pruebas de BCT.
                **** NOTA IMPOORTANTE ****
Si en algún momento desea cambiar  el correo del remitente,  debe cambiar en el
constructor  de la  clase, en la  sección comentada como  Parámetros del correo
deberá cambiar el diccionario msg con  la etiqueta  From por  el correo  al que
desea cambiar, además deberá  colocar la contraseña del correo en password. Por
último debera permitir el acceso fácil del correo en cuestión.
@author: LFLQ
"""

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class sentmail:
    def __init__(self):
        now = datetime.now()
        months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        month = months[now.month - 1]
        self.tiempo = now.strftime('%H:%M')
        self.fecha = "{} de {} del {} a las ".format(now.day, month, now.year)
        
        # Instancia varriable para llevar el mensaje
        self.msg = MIMEMultipart()
         
        # Parámetros del correo
        self.password = "archimex96"
        self.msg['From'] = "lfdo.luna@archimex.com.mx"
        #self.msg['To'] = destinatario
        self.msg['Subject'] = "Informe del ensayo BCT"
        
    def destino(self, correo):
        self.msg['To'] = correo
        
    def sent(self, direc):
        
        # Cuerpo del correo
        self.msg.attach(MIMEText('En este correo se adjunta el informe del ensayo de BCT con fecha {} a las {}'.format(self.fecha, self.tiempo), 
                                 'plain', 
                                 'utf-8'))
        
        # Adjuntar archivo
        att1 = MIMEText(open(direc, 
                             'rb').read(), 
                             'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        
        # Agregamos al correo
        att1["Content-Disposition"] = 'attachment; filename="BCT_informe del día {} a las {}.pdf"'.format(self.fecha, self.tiempo)
        self.msg.attach(att1)
        
        # creando server
        server = smtplib.SMTP('smtp.gmail.com: 587')
         
        server.starttls()
         
        # Iniciando seción 
        server.login(self.msg['From'], self.password)
         
         
        # Enviar correo mediante el server.
        server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
         
        server.quit()
         
        print "successfully sent email to %s:" % (self.msg['To'])