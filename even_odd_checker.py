#check if the number is even or odd
def even_odd_check(n):
    if(n%2)==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
        
num=input("Enter a number : ")
even_odd_check(float(num))