#prgram 9 area of traingle

def area_of_triangle(h,b):
    return 1/2*b*h

base = input("Enter the magnitude of taingle base ")
height = input("Enter the height of taingle height ")



print(f"area of traingle with heigh {height} and base {base} is {area_of_triangle(float(height),float(base))}")


