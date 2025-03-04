import serial
import smtplib
import time


EMAIL_ADDRESS = "joshadekoya5@gmail.com"
EMAIL_PASSWORD = "cpfk seyz dmfc oqnl"


TO_NUMBER = "7738583148@mailmymobile.net"

# Connect to Arduino (Check your COM port)
ser = serial.Serial("COM3", 9600, timeout=1)
time.sleep(2)  # Allow connection to stabilize

def send_alert():
    subject = "INTRUDER ALERT! "
    body = "Motion detected in your room!"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_NUMBER, message)

    print("Alert Sent!")

# Continuously check for motion
while True:
    try:
        line = ser.readline().decode("utf-8").strip()  # Read Arduino output
        if "INTRUDER ALERT!" in line:
            print("Motion detected! Sending alert...")
            send_alert()
            time.sleep(10)  # Prevent spamming alerts
    except Exception as e:
        print(f"Error: {e}")
