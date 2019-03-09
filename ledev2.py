from gpiozero import LED
import time
led1=LED(18)
led2=LED(23)
led3=LED(24)
#print(i)
led1.on()
led2.on()
led3.on()
print("Leds on")

time.sleep(200)
print("LED off")
#led.off()
