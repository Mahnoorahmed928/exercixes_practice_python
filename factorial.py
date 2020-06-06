#factorial of a number

    
def fact(n):
         res=1
         if n == 0:         #entered number 0 then fact =1
                return 1
         else:
            
             for i in range(1,n+1):
                res=res*i


             return res
        
try:
    
    n=int(input("enter a number "))
    print(f"Factorial of {int(n)} is {fact(n)}")
    
except:
    print("invalid entry")

    