# مرتب سازی سه عدد بدون استفاده از دستورات شرطی و حلقه 
a=int(input("enter a : "))
b=int(input("enter b : "))
c=int(input("enter c : "))
min1=min(a,b,c)
max1=max(a,b,c)
vasati=(a+b+c)-(min1+max1)
print("the sorted numbers : ",min1,vasati,max1)