# -*- coding: utf-8 -*-
"""

"""
def check_num(num):
    if num>0:
        print("Numer is positive")
    elif num<0:
        print("Numer is negative")
    elif num==0:
        print("Numer is zero")
     
try:
        
    num=float(input("ENter your number "))
    check_num(num)
    
except:
     print("error")
