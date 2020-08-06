# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:16:07 2020

@author: User
"""
#Realpe Josselyn- Grupo 2
#Datos de prueba.-
#Cantidad de llantas: 9
#Precio unitario: 100
#Valor a pagar: 810.0

#Cantidad de llantas: 2
#Precio unitario: 100
#Valor a pagar: 200.0

c=int(input("cantidad de llantas: "))
p=float(input("precio unitario: "))
if c>=4:
    print(0.9*p)
v=c*p
print("valor a pagar: ", v)
    
