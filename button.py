#!/usr/bin/env python

# Autor    :  Villarreal Luciano
# Creditos :  Villarreal Luciano

import os
import sys

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

button = port.PA10

gpio.init()
gpio.setcfg(button, gpio.INPUT)

while True:
	if gpio.input(button) == 1:
		sleep(0.05)
		if gpio.input(button) == 1:
			#os.system('./TakePic.py')
			print('Entro')
			os.system('./led.py on')
			sleep(0.5)
			os.system('./led.py off')
			sleep(0.5)
			os.system('./led.py on')
			sleep(0.5)
			os.system('./led.py off')
