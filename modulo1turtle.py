# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:26:15 2020

@author: USA
"""

from turtle import *
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
