# import serial
# import adafruit_thermal_printer

import sys
from pathlib import Path

#-------- shared utils access hack
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from shared import utils

printers = utils.setupPrinters();

s1 = "I don't know my ancestors and I wish I knew more about them. But I wonder how I can bring up that question and who do I ask?"
s2 = "I usually call my mother with bad news, or my friend Joe. When I want to tell them the worries I have, I know theyll listen with care and call me on my bullshit whenever I need them to. And they'll take a moment to mourn with me"
s3 = "I am really great at working between the hours of 9pm and 2am. There's something about that time that really works with my brain. Maybe it's because I never used to sleep at good hours, I used to only sleep for 4 so 5 hours each night. Even when I could sleep more, I'd take that extra time to read or surf the web instead. "

lineGroup = [
    utils.textWrapped(s1).splitlines(),
    utils.textWrapped(s2).splitlines(),
    utils.textWrapped(s3).splitlines()
]

utils.printInCycle(lineGroup, printers)