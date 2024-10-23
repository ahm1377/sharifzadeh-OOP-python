# برنامه ای بنویسید که حقوق نا خالص کارمندی را از ورودی دریافت کند . هر ماه بابت بیمه 7 درصد 
#و بابت وام مسکن 5 درصد آن را ، از حقوق نا خالص وی کم کند . مقدار بیمه ، وام مسکن و
#حقوق دریافتی او را محاسبه و چاپ کنید 
w=int(input("enter hoghogh nakhales : "))
bimeh = 0.07*w
maskan = 0.05*w
net = w-(bimeh+maskan)
print(" bimeh = ",bimeh,'\n',"maskan = ",maskan,'\n',"net = ",net)
