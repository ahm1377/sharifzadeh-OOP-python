# تبدیل شمسی به میلادی
shamsi=int(input("enter your birthday in shamsi : "))
ch=input("is your birthday before first january (y/n)? ")
if(ch=='y' or ch=="Y"):
    miladi=shamsi+621
else:
    miladi=shamsi+622
print(" miladi = ",miladi)