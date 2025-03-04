# motion_sensor_project1
The PIR sensor detects movement, specifically the motion of a door handle being turned.
If motion is detected, the Arduino turns on an LED as a visual indicator.
The Arduino sends a signal to Python via Serial communication.
The Python script then sends an SMS alert to notify the user of a potential intruder.
Components Used:
Arduino Mega 2560
PIR Motion Sensor
LED for visual indication
Breadboard & Jumper Wires for connections
Python with smtplib (Email-to-SMS method for alerts)
