# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:38:40 2015

@author: anyuser
"""

#from pylab import *
import matplotlib.pyplot as plt

import time

#ion()

simulationTime_ms = 0
simulationSpeed = 1


timeList_ms = []
speedList = []

fig = plt.figure(1)

plot221 = plt.subplot(221)
line, = plt.plot(timeList_ms, speedList, 'bo')
plt.title('Motorctrl_Fast')
plt.grid(True)

plot221.axes.set_xlim([0,1000])
plot221.axes.set_ylim([-100,+100])



#line, = plot(0,0)
for i in range(1,10):
    ######################
    #Perform Calculations
    #line.set_ydata(sin(x+i/10.0))  # update the data
    
    ######################
    #Do the plotting stuff
    timeList_ms.append(simulationTime_ms)
    speedList.append(simulationSpeed * i)
    line.set_xdata(timeList_ms[:])
    line.set_ydata(speedList[:])
    plot221.axes.set_xlim([0,1000])
    plt.draw()
    print "turn"
    
    ######################
    #Housekeeping
    simulationTime_ms += 100
    time.sleep(0.3)

