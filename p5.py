# برنامه ای بنویسید که یک عدد دو رقمی از ورودی دریافت کند . مقلوب آن را محاسبه کرده و نمایش دهد 
n=int(input("enter n : "))
r=n%10
q=n//10
print("reverse of n :",r*10+q)