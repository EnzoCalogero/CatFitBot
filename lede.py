import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ledPin=12
GPIO.setup(ledPin,GPIO.OUT)
GPIO.output(ledPin,GPIO.HIGH)

print("Led on")

time.sleep(1)
print("LED off")
GPIO.output(ledPin,GPIO.LOW)

