# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:23:37 2020

@author: User
"""
swich=[]
router=[]
lista=["R1","R2","R3","R4","R5,","S1","S2","S3"]
for i in lista:
    if "S" in i:
        swich.append(i)
    else:
        router.append(i)
print(swich)
print(router)

