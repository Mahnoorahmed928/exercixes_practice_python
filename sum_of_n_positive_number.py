#14 sum of n positive numbers

def positive_sum(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
        
    return sum
num=int(input("Enter the value of n : "))
print(f"sum of n positive integrers till {num} is {positive_sum(int(num))}")