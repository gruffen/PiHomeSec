#!/usr/bin/python3

import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

print('Press Ctrl-C to quit...')
f1 = open("output.txt", "w+")
f2 = open("time.txt", "w+")
timestep = 0
while True:
    f2.write(str(timestep) + '\n')
    # Read the difference between channel 0 and 1 (i.e. channel 0 minus channel 1).
    # Note you can change the differential value to the following:
    #  - 0 = Channel 0 minus channel 1
    #  - 1 = Channel 0 minus channel 3
    #  - 2 = Channel 1 minus channel 3
    #  - 3 = Channel 2 minus channel 3
    value = adc.read_adc_difference(0, gain=GAIN)
    # Note you can also pass an optional data_rate parameter above, see
    # simpletest.py and the read_adc function for more information.
    # Value will be a signed 12 or 16 bit integer value (depending on the ADC
    # precision, ADS1015 = 12-bit or ADS1115 = 16-bit).
    #print('Channel 0 minus 1: {0}'.format(value))
    # Pause for half a second.

    output = ((value*15) + value) / 16
    f1.write(str(output) + '\n')
    
    
    timestep = timestep + 0.5

    time.sleep(0.5)
