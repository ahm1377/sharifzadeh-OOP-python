# برنامه ای بنویسید که مختصات دو نقطه a و b را را خوانده ، طول مستقیم بین 
#آن ها را محاسبه کرده و نتیجه را نمایش دهد 
x1=float(input(" enter x1 : "))
y1=float(input(" enter y1 : "))
x2=float(input(" enter x2 : "))
y2=float(input(" enter y2 : "))
len=((x1-x2)**2+(y1-y2)**2)**(1/2)
print("the length of line =",len)
