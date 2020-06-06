#exercise 6
#copy string n times

def str_copy(st,n):
     print(f"{n} copies of {st} are {st*n}" )

st=input("Enter string : ")
while True:
    n=(input("how many copies do you want :"))
   
    try:
            val=int(n)
            if not(int( n)>0):
              print("input is negative only whole numbers are allowed")
              continue
        
    except ValueError:
        try:
            val=float(n)
            print("input is a float only whole numbers are allowed ")
            continue
        except ValueError:
            print("please enter valid number  whole numbers are allowed : ")
            continue
        
    break
str_copy(st,int(n))


