# برنامه ای بنویسید که طول اضلاع یک مثلث را خوانده و محیط و مساحت آن را مجاسبه کرده و نمایش 
#دهد برای محاسبه مساحت مثلث از فرمول زیر استفاده نمایید که در آن a و b و c طول اضلاع مثلث و p نصف محیط آن است 
a=float(input("enter a : "))
b=float(input("enter b : "))
c=float(input("enter c : "))
mohit=a+b+c
p=mohit/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
print(" mohit = ", mohit,"\n","masahat = ",s)
