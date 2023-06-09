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
    sender_email = 'your email address'
    sender_name = 'your name'
    sender_app_password = cred.GOOG
    recipient_email ='target address'
    email_subject ='You got Mail'

    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)
    smtp.login(sender_email, sender_app_password)
    smtp.to(recipient_email)
    smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
    smtp.write("Subject:" + email_subject + "\n")
    
    current_time = utime.localtime()
    formatted_time = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
    smtp.write("\nHello [YOUR NAME]" + "\n\nYou got new mail at " + formatted_time + ".\nCheck your mailbox")
    
    smtp.send()
    smtp.quit()
    
led = machine.Pin("LED", machine.Pin.OUT)
pin = machine.Pin(28, machine.Pin.IN)

if pin.value():
    for x in range(15):
        led.toggle()
        sleep(0.01)
        
for x in range(16):
    led.toggle()
    sleep(0.2)
