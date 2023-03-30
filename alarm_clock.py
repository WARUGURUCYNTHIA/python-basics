import datetime
import time
import playsound
 
def set_alarm(alarm_time):
    
 
 while True:
     current_time = datetime.datetime.now().strftime('%H:%M:%S')
     if current_time== alarm_time:
         print("wake up!")
         playsound.playsound('alarm_sound.mp3')
         break
     time.sleep(1)
     
 alarm_time = input("Enter the time for the alarm (in the format 'HH:MM:SS): ")
 
 set_alarm(alarm_time)         