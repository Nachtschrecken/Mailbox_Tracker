# Automatically track if you got new mail using Raspberry Pi Pico W and MicroPython
# Install IR sensor on your Pico and get started
#
# Copyright (c) Ferris Kleier 2023
# License: MIT

import cred
import umail
import network
import utime
from utime import sleep

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(cred.SSID, cred.PASS)
while wlan.isconnected() == False:
    sleep(1)

def sendmail():
    sender_email = cred.EMAIL
    sender_name = 'TrackBox'
    sender_app_password = cred.GOOG
    recipient_email = cred.EMAIL
    email_subject = 'You got Mail'

    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)
    smtp.login(sender_email, sender_app_password)
    smtp.to(recipient_email)
    smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
    smtp.write("Subject:" + email_subject + "\n")
    
    current_time = utime.localtime()
    formatted_time = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
    smtp.write("\nHello " + cred.NAME + "\n\nYou got new mail at " + formatted_time + ".\nCheck your mailbox")
    
    smtp.send()
    smtp.quit()
    
led = machine.Pin("LED", machine.Pin.OUT)
pin = machine.Pin(28, machine.Pin.IN)

while True:
    if pin.value():
        led.on()
        sendmail()
        sleep(20)
        led.off()
