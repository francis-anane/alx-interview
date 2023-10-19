#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# Loop 10,000 times
for _ in range(10000):
    # Introduce random delays
    sleep(random.random())

    # Generate and write log lines
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(
            1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))

    # Flush the buffer to ensure immediate printing
    sys.stdout.flush()
