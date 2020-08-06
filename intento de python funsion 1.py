# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:07:14 2020

@author: User
"""

def año = int(input("Escriba un año: "))

if año % 400 == 0 or (año % 100 != 0 and año % 4 == 0):
    print(año,"->",end="")
    print("True")
else:
    print(año,"->",end="")
    print("False")
    return año 

