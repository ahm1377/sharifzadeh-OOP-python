# محاسبه sin به توان cos و بالعکس
import math 
x=float(input("enter radian  : "))
print(" sin (x) = ", math.sin(x),"\n","cos (x) = ",math.cos(x))
y1=math.sin(x)**math.cos(x)
y2=math.cos(x)**math.sin(x)
print("      y1 = ",y1,"\n","     y2 = ",y2)