# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:38:40 2015

@author: anyuser
"""

#from pylab import *
import matplotlib.pyplot as plt
import time
import MotorCtrlFast as motorFast

#ion()

#SETTINGS
simulationTimeIncrement_ms = 100
simulationTargetSpeed = 100

#INIT
simulationTime_ms = 0
timeList_ms = []
speedList = []
motorFast.MotorCtrlFast_Init()
motorFastSpeed = 0


fig = plt.figure(1)

plot221 = plt.subplot(221)
line, = plt.plot(timeList_ms, speedList, 'bo')
plt.title('Motorctrl_Fast')
plt.grid(True)

#plot221.axes.set_xlim([0,100])
plot221.axes.set_ylim([-100,+100])



#line, = plot(0,0)
for i in range(1,10):
    ######################
    #Perform Calculations
    motorFastSpeed = motorFast.MotorCtrlFast_Cyclic(simulationTimeIncrement_ms, motorFastSpeed, simulationTargetSpeed)
    
    ######################
    #Do the plotting stuff
    timeList_ms.append(simulationTime_ms)
    speedList.append(motorFastSpeed)
    line.set_xdata(timeList_ms[:])
    line.set_ydata(speedList[:])
    plot221.axes.set_xlim([0,simulationTime_ms+100])
    plt.draw()
    print "turn"
    
    ######################
    #Housekeeping
    simulationTime_ms += 100
    time.sleep(0.3)
