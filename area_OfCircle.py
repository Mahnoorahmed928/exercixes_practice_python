# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:56:22 2020

@author: Abdullah
"""

#calculate area of circle
pi=22/7
def area(radius):
   return pi*radius*radius

rad = float(input("Enter raidus  "))
print(f"the area is  {area(rad)}")
