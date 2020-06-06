#count number of letters and digits in str
statement=input("enter string: ")

count_digit=0
count_alphabet=0

for s in statement:
    
    if s.isalpha():
        count_alphabet+=1
    if s.isdigit():
        count_digit+=1
    
print(f"digit count ={count_digit} , alphabet count ={count_alphabet}")
# dir(st)