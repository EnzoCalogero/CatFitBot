from gpiozero import Button
import time 
button = Button(22, pull_up=False)
#pin= 2 (vv)
#pin= 15 (pulsante)

while True:
    time.sleep(1)
    if button.is_pressed:
        print("verticale!")
    else:
         print("exit")

