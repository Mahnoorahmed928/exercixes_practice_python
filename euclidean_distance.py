#program 11 euclidean distance

import math
def euclidean_distance(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

x1=float(input("Enter C0-ordinate for x1 "))
x2=float(input("Enter co-ordinate for x2 "))
y1=float(input("Enter C0-ordinate for y1 "))
y2=float(input("Enter co-ordinate for y2 "))
print(f"The euclidean distance between point ({x1},{x2}) and ({y1},{y2}) is {euclidean_distance(x1,x2,y1,y2)}")
