# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:17:27 2020

@author: User
"""

aclNum = input("ingrese el numero de ACL ")
aclNum=int(aclNum)
if aclNum >= 1 and aclNum <= 99:
    print("es ACL STANDARD")
elif aclNum >=100 and aclNum <= 199:
    print("es ACL EXTENDIDA.")
else:
    print("no es ACL.")
