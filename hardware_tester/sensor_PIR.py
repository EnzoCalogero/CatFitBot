import time
from gpiozero import MotionSensor
pir= MotionSensor(4)

while True:
    pir.wait_for_motion()
    
    print("detect")
    time.sleep(.3)
    
def motion():
    from gpiozero import MotionSensor
    pir = MotionSensor(4)
    pir.wait_for_motion()
    print("detect")
    return 0
        