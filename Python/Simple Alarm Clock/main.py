import datetime as dt
from time import sleep
import os

# Input for alarm time
hours = int(input("Enter the hour for the alarm: "))
minutes = int(input("Enter the minutes for the alarm: "))
am_or_pm = input("AM or PM? ").strip().lower()

# Convert to 24-hour format
if am_or_pm == "pm":
    hours += 12

os.system("cls" if os.name == "nt" else "clear")  # Clear the screen

while True:
    now = dt.datetime.now()
    if now.hour == hours and now.minute == minutes:
        print("WAKE UP!!!")
        while True:
            # Play the alarm sound repeatedly
            try:
                ps.playsound("Alarm-Clock Sound!!!.mp3")
            except KeyboardInterrupt:
                break  # Exit the alarm on user interruption
            sleep(2)
    sleep(1)  # Wait for 1 second before checking the time again

            


