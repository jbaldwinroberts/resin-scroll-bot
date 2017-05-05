#!/usr/bin/env python

import time
import signal
import os
import subprocess
import threading

import scrollphathd
from scrollphathd.fonts import font5x7

scrollphathd.rotate(float(os.environ["rotation"]))
scrollphathd.set_brightness(float(os.environ["brightness"]))
width = scrollphathd.get_shape()[0]

command = ["./cryptocurrency-tracker", "-c"]
command.extend(os.environ["cryptos"].split())
command.extend(["-f", os.environ["format"]])

output = ["", ""]
index = 0

def worker(e):
    global output
    global index

    while True:
        output[index] = subprocess.check_output(command).strip("\n")
        e.wait()

def display(e):
    global output
    global index

    while True:
        message = output[index]
        index = 1 - index
        e.set()
        e.clear()

        scrollphathd.clear()
        length = scrollphathd.write_string(message, x=width, font=font5x7)

        scrollphathd.scroll_to(0, 0)
        for i in range(length + width):
            scrollphathd.show()
            time.sleep(0.05)
            scrollphathd.scroll()

e = threading.Event()
t1 = threading.Thread(name='worker', target=worker, args=(e,))
t2 = threading.Thread(name='display', target=display, args=(e,))
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()

while True:
    time.sleep(1)
