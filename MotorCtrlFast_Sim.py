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
plotWindowLength_ms = 2000

#INIT
simulationTime_ms = 0
timeList_ms = []
speedList = []
motorFastSpeed = -100


fig = plt.figure(1)

plot221 = plt.subplot(221)
data221, = plt.plot(timeList_ms, speedList, 'bo')
plt.title('Motorctrl_Fast')
plt.grid(True)

#plot221.axes.set_xlim([0,100])
plot221.axes.set_ylim([-110,+110])



#line, = plot(0,0)
for i in range(1,300):
    ######################
    #Perform Calculations
    motorFastSpeed = motorFast.MotorCtrlFast_Cyclic(simulationTimeIncrement_ms, motorFastSpeed, simulationTargetSpeed)
    
    ######################
    #Do the plotting stuff
    timeList_ms.append(simulationTime_ms)
    speedList.append(motorFastSpeed)
    data221.set_xdata(timeList_ms[:])
    data221.set_ydata(speedList[:])
    if (simulationTime_ms < plotWindowLength_ms):
        plot221.axes.set_xlim([0,plotWindowLength_ms])
    else:
        plot221.axes.set_xlim([simulationTime_ms-plotWindowLength_ms,simulationTime_ms+100])
        
    plt.draw()
    #print "turn"
    
    ######################
    #Housekeeping
    simulationTime_ms += 100
    time.sleep(0.1)


    if i == 50:
        simulationTargetSpeed = -50
    if i == 100:
        simulationTargetSpeed = -100
    if i == 150:
        simulationTargetSpeed = 0

print "done"