#!/usr/bin/env python


# Autor    :  Villarreal Luciano
# Creditos :  Villarreal Luciano

import os
import sys

from argparse import ArgumentParser

from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PA6

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)

parser = ArgumentParser(description = '%(prog)s is an ArgumentParser demo')
parser.add_argument('arg1',choices=['on','off'])

args = parser.parse_args()

if args.arg1 == 'on':
	print 'funciona - on'
	gpio.output(led, 1)
elif args.arg1 == 'off':
	print 'funciona - off'
	gpio.output(led, 0)

