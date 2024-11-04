# حافظه مصرفی اشیا
import sys
x=int(input("enter an integer : "))
y=float(input("enter a float    : "))
str=input("enter a string   : ")
print("the size of memory of x= ",sys.getsizeof(x),"bytes")
print("the size of memory of y= ",sys.getsizeof(y),"bytes")
print("the size of memory of str= ",sys.getsizeof(str),"bytes")