# Run this file to execute the Spidermae script at regular intervals of your
# choice.

import datetime
import time
import math
import subprocess
import platform
import sys

from settings import setrun

timeInterval = setrun()

os = platform.system()
intpath = sys.executable

current = math.floor(time.time())
interval = timeInterval * 60 * 60
next = current + 2

print("Setting up...")

while next >= current:
    if next == current:
        print("Running Spidermae...")

        try:
            job = subprocess.Popen([intpath,"./Spidermae.py"])
            job.wait()
        except Exception as e:
            print("Please enter the path to your Python interpreter in run.py manually!")

        next += interval

    else:
        t = next - current
        time.sleep(1)
    current = math.floor(time.time())
