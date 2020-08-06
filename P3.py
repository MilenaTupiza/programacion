# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:31:06 2020

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
        
        
def diadelmes(año, mes):
    if año < 1900 or mes < 1 or mes > 12:
        return
    dias= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res= dias[mes-1]
    if mes == 2 and aniobi(año):
        res = 29
    return res
print(diadelmes(2019,2))

años= [1900, 2000, 2016, 1987]
meses= [2, 2, 1, 11]
resultado= [28, 29, 31, 30]
for i in range(len(años)):
    año= años[i]
    me= meses[i]
    print(año,me," -> ", end=" ")
    resultadofinal= diadelmes(año, me)
    if resultadofinal == resultado[i]:
        print("OK")
    else:
        print("FAILED")

def diadelaño (año, mes, dia):
    dias=0
    for m in range(1, mes):
        diames= diadelmes(año,m)
        if diames == None:
            return None
        dias += diames
        
    diames= diadelmes(año, mes)
    if dia >=1 and dia <= diames:
        return dias + dia
    else:
        return None
print(diadelaño(2020,6,8))
