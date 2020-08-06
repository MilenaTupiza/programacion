# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:04:00 2020

@author: User
"""

año = int(input("Escriba un año: "))

if año % 400 == 0 or (año % 100 != 0 and año % 4 == 0):
    print(año,"->",end="")
    print("OK")
else:
    print(año,"->",end="")
    print("Failed")
