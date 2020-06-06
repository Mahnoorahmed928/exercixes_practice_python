#  to check whether a string in palindrome or not
def palindrome(st):
    lst = list(st)          #first converts string inot list
    lst.reverse()          #then reverse of lst
    rvrse = ''.join([str(l) for l in lst])         #converts list back to string
    if st == rvrse:                                    #checking
        print(f"{st} is palindrome")
    else:
        print(f"Text {st} is not palindrome")
        
st = input("Enter text : ")
palindrome(st)