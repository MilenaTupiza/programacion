# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:47:23 2020

@author: User
"""
dato=int(input("ingrese el numero de veces que contare: "))
contador=1
acumulador=0
while contador<=dato:
    print(contador,end=" ")
    acumulador+=contador
    contador+=1
print("la suma de los # es: ",acumulador)
