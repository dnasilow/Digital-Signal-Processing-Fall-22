# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:53:31 2022

@author: Arihant
"""

## use pysimplegui or other libraries to create a user interface
## capture a snippet of sound (eg, 5 seconds)
## GUI to process the recorded snippet 
## phaser done, distortion, delay to be figured out


from pyo import *
from scipy.io.wavfile import read, write

s = Server().boot()
s.start()
sf = SfPlayer("follies_intro.wav", speed=1, loop=True)
s = Server().boot()
s.start()
snd = SndTable("follies_intro.wav")
env = HannTable()
pos = Phasor(freq=snd.getRate()*.25, mul=snd.getSize())
dur = Noise(mul=.001, add=.1)
g = Granulator(snd, env, [1, 1.001], pos, dur, 32, mul=.5)
d = Disto(sf, .75, .5, 1, 0)
#de = Delay(sf, 0.25, 0, 1, 1, 0)
#rev = reversed()
