# زمان صرف شده برای اجرای دستورات  
import time
start_time=time.time()
n=int(input("enter n : "))
m=n**n
print("m = ",m)
end_time=time.time()
real_time=end_time-start_time
print("time: ", real_time)
