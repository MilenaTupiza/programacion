# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:37:27 2020

@author: User
"""
def direccion(calle,sector,codigopostal,referencia,numcasa):
    print("Su direccion es: ","Su sector es: ",sector,"Calle ",calle)
    print("Su casa es la numero: ",numcasa,"con codigo postal numero: ",codigopostal)
    print("y esta crca de: ",referencia)
print("Ingrese los datos que se solicitan de direccion: ")
c=input("Ingrese la calle: ")
s=input("Ingrese sector de residencia: ")
cod=input("Ingrese codigo postal: ")
r=input("Ingrese una referencia de su domicilio: ")
num=input("Ingrese el  numero de casa: ")

direccion(c,s,cod,r,num)

