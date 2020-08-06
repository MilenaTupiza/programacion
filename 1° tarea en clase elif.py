# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:57:57 2020

@author: User
"""


nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
ubicacion=input("ingrese su ubicacion: ")
edad=input("ingrese su edad ")
print("hola soy "+nombre+" "+apellido+", vivo en la ciudad de "+ubicacion+" y mi edad es "+edad)
edad=int(edad)
if edad >=1 and edad <=6:
    print(" y soy niño")
elif edad >=7 and edad <=13:
        print(" y soy preadolescente")
elif edad >=14 and edad <=18:
           print(" y soy adolescente")
elif edad >=19 and edad <=26:
               print(" y soy adulto")
else:
    print(" y soy adulto mayor")