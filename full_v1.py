#!/usr/bin/env python

#import math
import time
import random
import logging
from gpiozero import LED

from gpiozero import MotionSensor
import pantilthat


# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()  # handler for routine view
f_handler = logging.FileHandler('CatFitBot.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.info('This is a warning')
logger.error('This is an information')



pir = MotionSensor(4)
led1 = LED(18)
logger.error('starting Application')
while True:
    #led1.off()
    print("waiting")
    pir.wait_for_motion()
    logger.error('starting Routine')

    led1.on()
    print("Led 1 on")

    # Reset the time
    t = time.time()
    t2 = time.time()

    a1 = random.randint(40, 90) * (-1)

    k = random.randint(1, 10)
    b1 = random.randint(0, 80) - 40
    while t2 - t < 60:
        logger.error('starting Application for 1 minute')
        print("Time: t2--> {} t--> {} delta--> {}".format(t2, t, t2 - t))
        # Get th
        a2 = random.randint(40, 90) * (-1)

        k = random.randint(1, 10)
        b2 = random.randint(0, 80) - 40
        print("{}  {}".format(a1, b1))
        print("{}  {}".format(a2, b2))

        a_step = (a1 - a2) / 10
        b_step = (b1 - b2) / 10

        # micro movement
        for i in range(10):
            print("init {} finale{} step {} posizione {} delta {}".format(a1, a2, i, int(a1 - i * a_step), a_step))
            pantilthat.pan(int(b1 - i * b_step))
            pantilthat.tilt(int(a1 - i * a_step))

            # Two decimal places is quite enough!
            print(round(b1, 2))

            # Sleep for a bit so we're not hammering the HAT with updates
            # GPIO.output(ledPin,GPIO.LOW)
            time.sleep(0.1)
        a1 = a2
        b1 = b2
        k = random.randint(1, 10)
        time.sleep(5 / k)
        t2 = time.time()

