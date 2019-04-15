#!/usr/bin/env python
import random
import time

import pantilthat

t = time.time()
a1 = random.randint(40, 90) * (-1)

k = random.randint(1, 10)
b1 = random.randint(0, 80) - 40
while True:

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

        time.sleep(0.1)

    a1 = a2
    b1 = b2
    k = random.randint(1, 10)
    time.sleep(5 / k)
