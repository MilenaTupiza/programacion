# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:03:51 2020

@author: User
"""
dato=input("ingrese el numero de veces que contare: ")
contador=1
acumulador=0
while True:
    print (contador)
    contador+=1
    if contador >= dato:
        break
print("la suma de los # es: ",acumulador+contador)
print("el promedio es: ",acumulador/dato)
