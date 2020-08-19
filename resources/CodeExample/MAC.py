#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:29:59 2020

@author: pi
"""
import socket
print '*****************************************'
hostname = socket.gethostname()
print('Nombre dispositivo:' + hostname)
ipaddress = socket.gethostbyname(hostname)
print('Dirección IP: ' + ipaddress)

def getMAC(interface = 'wlan0'):
    try:
        str = open('/sys/class/net/%s/address' %interface).read()
    except:
        str = "None"
    return str[0:17]
print "MAC: " + getMAC('wlan0')