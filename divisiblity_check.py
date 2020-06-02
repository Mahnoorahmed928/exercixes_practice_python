# -*- coding: utf-8 -*-
"""

"""

def divisiblity_check(num1,num2):
    if num1%num2==0:
        print(f"number {num1} is completely divisible by {num2}")
    else:
        print(f"number {num1} is not  completely divisible by {num2}")
        
        
while True:
    num1=input("Enter numerator--" )
    
    if not(num1.isdigit()):
      print("only integers are allowed")
      continue
        
    
    num2=input("Enter denumerator--" )
    
    if not(num2.isdigit()):
        print("only integers are allowed\n")
        continue
    else:
        break
    
    
divisiblity_check(int(num1),int(num2))