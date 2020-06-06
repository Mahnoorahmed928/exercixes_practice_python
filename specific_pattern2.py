#example 21 generating specific pattern"
'''
*
**
***
****
*****
'''
i=1
j=1
while i<=5:
    j=1
#     if (i==3):
#         continue
#         pass
    
    while j<=i:
        print("*",end="")
        j+=1
    print("")
    
    i+=1
  
i=2
j=2
while i<=5:
    j=5
    while j>=i:
        print("*",end="")
        j-=1
    print("")
    
    i+=1
    