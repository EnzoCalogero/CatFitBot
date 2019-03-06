from gpiozero import LED
import time
led=LED(18)
#print(i)
led.on()
print("Led on")

time.sleep(2)
print("LED off")
led.off()
