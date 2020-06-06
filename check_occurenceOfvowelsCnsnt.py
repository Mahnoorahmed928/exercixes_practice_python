#check the occurence of vowels and consonents

def check_vow_cons(st):
    count_vow=0
    count_con=0
    for ch in st:
        
        if(ch=='a'or ch=='e'or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
            count_vow+=1
            
        if(ch=='b'or ch=='c' or ch=='d'or ch=='d' or ch=='f' or ch=='g' or ch=='h' or ch=='j' or ch=='k'
           or ch=='l'or
          ch=='m' or ch=='n' or ch=='p' or ch=='q' or ch=='r' or ch=='s' or ch=='t' or ch=='u' or ch=='v' or ch=='w'
           or ch=='x'or ch=='y'or ch=='z' or ch=='B'or ch=='C' or ch=='D'or ch=='F'or ch=='G' or ch=='H' or ch=='J'
           or ch=='K'
           or ch=='L' or
          ch=='M'or ch=='N' or ch=='P' or ch=='Q' or ch=='R' or ch=='S' or ch=='T' or ch=='U' or ch=='V' or ch=='W'
           or ch=='X'or ch=='Y'or ch=='Z' ):
             count_con+=1
    print(f"Vowels {count_vow}")
    print(f"consonents{count_con}")
    
inp=input("Enter  string ")
check_vow_cons(inp)