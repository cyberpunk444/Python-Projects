# Timer
# -------------
import os
import time
inp_h = int(input("Enter hours (0 for less than 1h): "))
inp_m = int(input("Enter minutes (0 for less tham 1m) : "))
inp_s = int(input("Enter seconds :"))

countdown = (inp_h * 60 * 60) + (inp_m * 60) + (inp_s)

for i in range(countdown,0,-1):
    print(i)
    time.sleep(1)
    if i == 1:
        os.startfile("C:\\Users\\aniket\\Desktop\\Python Projects\\100 mini projects\\project 11\\timer.mp3")
print("Timer reached.")