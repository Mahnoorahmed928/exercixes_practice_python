# -*- coding: utf-8 -*-
"""

"""
#calculate volumne of sphere

#v=4/3*pi*r*r*r
pi=22/7

def vol_sphere(r):
    return 4/3*pi*r*r*r
rad=float(input("enter radius : "))
print("volume is :")
vol_sphere(rad)