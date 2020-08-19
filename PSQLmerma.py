#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:45:37 2020
Archivo: PSQLmerma.py
Comentarios: Clase que implementa la cosulta de el nobre del cliente y el pedido
en la base de datos de merma, para la la GUI del BCT
@author: LFLQ
"""

import psycopg2
import tkMessageBox

class PSQLmerma:
    def __init__(self):                
        # Credenciales de acceso a Postgres
        self.PSQL_HOST = "192.168.5.243"
        self.PSQL_PORT = "5432"
        self.PSQL_USER = "postgres"
        self.PSQL_PASS = "bi"
        self.PSQL_DB   = "merma"
        self.cliente = 'N/A'
        self.producto = 'N/A'
    
    def consulta(self, campo, pedido):
        try:
            # Conectarse a la base de datos
            connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (self.PSQL_HOST, self.PSQL_PORT, self.PSQL_USER, self.PSQL_PASS, self.PSQL_DB)
            conn = psycopg2.connect(connstr)
            
            # Abrir un cursor para realizar operaciones sobre la base de datos
            cur = conn.cursor()
            
            # Ejecutar una consulta SELECT
            sqlquery = "SELECT producto, cliete, pedido FROM programa_produccion WHERE {} LIKE '%{}%';".format(str(campo), str(pedido))
            cur.execute(sqlquery)
            
            # Obtener los resultados como objetos Python
            row = cur.fetchone()
            
            # Recuperar datos del objeto Python
            answ=tkMessageBox.askyesno("Atención", 
                                       "El pedido {} corresponde al cliente {}, del producto {}, ¿Es correcta la información?".format(row[2], row[1], row[0]))
            if answ==True:
                tkMessageBox.showinfo('Atención', 'Datos recopilados')
                self.cliente = str(row[1])
                self.producto = str(row[0])
            
            
            # Hacer algo con los datos
            print 'Cliente: ' + self.cliente
            print 'Producto: ' + self.producto
        
        except:
            print("Error de base de datos")
            
        finally:
            if (cur):
                cur.close()
                print "Cursor cerrado"
            if (conn):
                conn.close()
                print("Conexión a la base de datos cerrada")