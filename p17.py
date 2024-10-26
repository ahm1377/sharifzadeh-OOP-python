# nامین بیت یک عدد را برابر 1 کردن 
num=int(input("enter a number : "))
print("binary before : ",bin(num))
n=int(input("enter nth bit to set : "))
num=(1<<n)|num
print("binary after : ",bin(num))  