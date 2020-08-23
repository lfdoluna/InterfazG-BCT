#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:50:27 2020

@author: pi
"""
# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib
from email.header import Header
 
# create message object instance
msg = MIMEMultipart()
 
 
# Parámetros del correo
password = "archimex*19"
msg['From'] = "practicantes.bi@archimex.com.mx"
msg['To'] = "lflunaq@gmail.com"
msg['Subject'] = "Prueba correo archivo adjunto"

# Cuerpo del correo
msg.attach(MIMEText('Correo de prueba en el envio de archivo adjunto', 'plain', 'utf-8'))

# Adjuntar archivo
att1 = MIMEText(open('/home/pi/Desktop/Reportes_Generados/2020/Agosto/BCT_reporte_19-Agosto-2020_13.18.pdf', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'

# Agregamos al correo
att1["Content-Disposition"] = 'attachment; filename="BCT_reporte.pdf"'
msg.attach(att1)

# creando server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Iniciando seción 
server.login(msg['From'], password)
 
 
# Enviar correo mediante el server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print "successfully sent email to %s:" % (msg['To'])