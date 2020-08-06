# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:33:51 2020

@author: User
"""
#Realpe Josselyn- Grupo 2
#Datos de prueba.-
#Horas trabajadas: 68
#Tarifa por hora: 6
#Descuentos: 60
#Valor a pagar: 432.0

h=float(input("horas trabajadas: "))
t=float(input("tarifa por hora: "))
d=float(input("descuentos: "))
if h<=40:
    print(h*t)-d
else:
    print("Valor a pagar: ", (40*t)+(1.5*t*(h-40))-d)