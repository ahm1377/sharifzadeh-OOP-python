# مرتب کردن سه عدد به ترتیب صعودی
a=int(input("enter a : "))
b=int(input("enter b : "))
c=int(input("enter c : "))
if(a>b):
    a,b=b,a
if(a>c):
    a,c=c,a
if(b>c):
    b,c=c,b
print("the sourted numbers: \n",a,"   ",b,"   ",c)