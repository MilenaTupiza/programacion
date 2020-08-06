# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:13:31 2020

@author: User
"""

hostnames=["R1","R2","R3","S1","S2","S3"]
print(type(hostnames))
print(len(hostnames))
print(hostnames)
print(hostnames[0])
print(hostnames[1])
print(hostnames[2])
print(hostnames[3])
print(hostnames[4])
print(hostnames[5])
print(hostnames[-1])
print(hostnames[-2])
print(hostnames[-6])
#print(hostnames[6])#me dara error porque no existe esta posicion(valor)
#print(hostnames[-7])#me dara error porque no existe esta posicion(valor)

hostnames[5]="S5"
del hostnames[5]

