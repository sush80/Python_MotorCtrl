# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:38:40 2015

@author: anyuser
"""

#from pylab import *
import matplotlib.pyplot as plt
import time
import MotorCtrl as motorFast

#ion()

#SETTINGS
simulationTimeIncrement_ms = 100
simulationTargetSpeed = 100
plotWindowLength_ms = 2000

#INIT
simulationTime_ms = 0
timeList_ms = []
speedList = []
setSpeedList = []
motorFastSpeed = -100


fig = plt.figure(1)

plot221 = fig.add_subplot(221)
data221A, = plot221.plot(timeList_ms, speedList, 'bo')
data221B, = plot221.plot(timeList_ms, setSpeedList, 'r+')
plot222 = fig.add_subplot(222)
data222, = plot222.plot(timeList_ms, speedList, 'ro')
#plot221.title('Motorctrl_Fast')
plot221.grid(True)

#plot221.axes.set_xlim([0,100])
plot221.axes.set_ylim([-110,+110])



#line, = plot(0,0)
for i in range(1,300):
    ############################################
    #Perform Calculations
    motorFastSpeed = motorFast.MotorCtrlFast_Cyclic(simulationTimeIncrement_ms, motorFastSpeed, simulationTargetSpeed)
    
    ############################################
    #Do the plotting stuff
    timeList_ms.append(simulationTime_ms)
    speedList.append(motorFastSpeed)
    data221A.set_xdata(timeList_ms[:])
    data221A.set_ydata(speedList[:])
    
    setSpeedList.append(simulationTargetSpeed)
    data221B.set_xdata(timeList_ms[:])
    data221B.set_ydata(setSpeedList[:])

    if (simulationTime_ms < plotWindowLength_ms):
        plot221.axes.set_xlim([0,plotWindowLength_ms])
    else:
        plot221.axes.set_xlim([simulationTime_ms-plotWindowLength_ms,simulationTime_ms+100])
        
    plt.draw()
    #print "turn"
    
    ############################################
    #Housekeeping
    simulationTime_ms += 100
    #time.sleep(0.01)


    ######################
    # Mess with simulation Parameters
    if i == 50:
        simulationTargetSpeed = -50
    if i == 100:
        simulationTargetSpeed = -100
    if i == 150:
        simulationTargetSpeed = 0

print "done"