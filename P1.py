# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:07:37 2020

@author: User
"""

def aniobi(anio):
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True 
a= aniobi(2020)
print(a)

datos=[2019, 2020, 2016, 1987]
resutado=[False,True, True, False]

for i in range(len(datos)):
    año= datos[i]
    print(año, " -> ", end=" ")
    resultadofinal= aniobi(año)
    if resultadofinal == resutado[i]:
        print("OK")
    else:
        print("FAILED")