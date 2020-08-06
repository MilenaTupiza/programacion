# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:24:30 2020

@author: User
"""

ipadd={"R1":"10.0.0.1","R2":"10.0.0.2",
       "R3":"10.0.0.3","S1":"10.1.0.1",
       "S2":"10.1.0.2"}
print(type(ipadd))

dict1={"usuario1":"1400730667","valor":5000,"edad":18,
      "soltera":True,"RATE en %":51.2}

print(ipadd["S2"])
ipadd["S5"]="10.1.0.5"
print("S1" in ipadd)
print("5000" in dict1)

