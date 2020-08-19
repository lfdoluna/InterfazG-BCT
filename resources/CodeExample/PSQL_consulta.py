#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:42:05 2020
Archivo: PSQL_consulta.py
Comentarios: Conexión a postgres en la base de datos del sistema de OEE
@author: pi
"""

import psycopg2

# Postgres
PSQL_HOST = "192.168.5.243"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "bi"
PSQL_DB   = "merma"
while True:
    try:
        # Conectarse a la base de datos
        connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
        conn = psycopg2.connect(connstr)
        
        # Abrir un cursor para realizar operaciones sobre la base de datos
        cur = conn.cursor()
        
        # Ejecutar una consulta SELECT
        gg = input("Ingrese número de pedido: ")
        if gg == 0:
            break
        sqlquery = "SELECT * FROM programa_produccion WHERE pedido LIKE '{}%';".format(str(gg))
        cur.execute(sqlquery)
        # Obtener los resultados como objetos Python
        row = cur.fetchone()
        records = cur.fetchall()
        print "Número de filas:  " + str(len(records))
        print "Imprime cada una de ellas"
        for row in records:
            print "Id: " + str(row[0])
            print "Pedido: " + str(row[1])
            print "Cliente: " + str(row[2])
            print "Producto: " + str(row[3])
            print "Fecha de entrega: " + str(row[4])
            print "Golpes programados: " + str(row[5])
            print "largo: " + str(row[6])
            print "Ancho: " + str(row[7])
            print "Piezas: " + str(row[8])
            print "Velocidad: " + str(row[9])
            print "tiempo cambio: " + str(row[10])
            print "min prod: " + str(row[11])
            print "inicio: " + str(row[12])
            print "final: " + str(row[13])
            print "maquina: " + str(row[14])
            print "turno: " + str(row[15])
            print "fecha produccion: " + str(row[16])
            print "Estado: " + str(row[17])
            print "tinta: " + str(row[18])
            print("\n")
        
        # Cerrar la conexión con la base de datos
        #cur.close()90
        #conn.close()
        
        # Recuperar datos del objeto Python
        username = row
        
        # Hacer algo con los datos
        print(username)
    
        
    except KeyboardInterrupt:
        break
        print ('Salida')
        
    except:
        print("Error de base de datos")
        
    finally:
        if (cur):
            cur.close()
            print "Cursor cerrado"
        if (conn):
            conn.close()
            print("The SQLite connection is closed")
            print '\n******************************************************'