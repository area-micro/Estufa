#!/usr/bin/env python

# Autor    :  Villarreal Luciano
# Creditos :  Villarreal Luciano

import os
import sys

from time import sleep

os.system('./led.py on')
sleep(5)
os.system('fswebcam imagen.jpg')
sleep(3)
os.system('./led.py off')


