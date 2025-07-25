import os
import time
from datetime import datetime

folder_path = r"C:\Users\Computer House\Documents"


print(f"Files in the Folder")
for file_name in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path,file_name)):
        print(file_name)


print("Printing time every 5 seconds for 1 minute:/n")

for _ in range(12):
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(5)



log_file = "timelog.log"

for _ in range(6):  # 60 seconds / 10 = 6 times
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, "a") as f:
        f.write(f"{current_time}\n")
    
    print(f"Logged: {current_time}")
    time.sleep(10)  # wait for 10 seconds


import smtplib
from email.message import EmailMessage
import time

def send_email():
    msg = EmailMessage()
    msg.set_content("Time to code your Python project! 💻")
    msg['Subject'] = "Daily Reminder"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = "receiver_email@gmail.com"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("your_email@gmail.com", "your_app_password")
        smtp.send_message(msg)
        print("Email sent!")

# Simulate daily reminder (e.g., send now for demo)
send_email()

