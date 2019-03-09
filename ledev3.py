from gpiozero import LED
import time
led3=LED(18)
led1=LED(24)
led2=LED(23)
#print(i)


while True:
    led1.on()
    led2.on()
    led3.on()
    print("Leds on1")
    time.sleep(0.3)
    #led1.off()
    #led2.on()
    print("led on 2")
    time.sleep(0.3)

time.sleep(200)
print("LED off")
#led.off()
