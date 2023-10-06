import time                                             #importing  time module
import os                                               #importing os module                   
alarm_time = input("Enter alarm time in [HH]:[MM] : ")  #Taking time from user to set it as the alarm timing
print("<- Alarm is Set 👍 ->")                          #printing alarm is set as a response to user


while True:                                             # Creating a loop until alarm rings
    current_time = time.strftime("%H:%M")               # assigning the current time using the time module's method time.strftime() method
    if current_time == alarm_time:                      #Cheching for condition untill current time and alarm time is equal
        print("Wake up")                                #printing wake up messsage to user which means alarm is ringing
        os.startfile("C:\\Users\\aniket\\Desktop\\Python Projects\\100 mini projects\\day 2\\alarm.mp3")    #opening the alarm audio at specified time
        break                                           #breaking the loop
    time.sleep(60)                                      #using time.sleep() method so that the loop doesnt run continuosly rather it runs for every 60s or 1 min to check time is reached or not , so that program doesn't uses unnessesary cpu usage ,it makes the program efficient.