#WAP using function to calculate distance b/w two end point.
import math
def distance(x1,x2,y1,y2):
    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return d
x1=int(input("enter x1:"))
y1=int(input("enter yi:"))
x2=int(input("enter x2:"))
y2=int(input("enter y2:"))
result=distance (x1,y1,x2,y2)
print("distance between two points=",result)
