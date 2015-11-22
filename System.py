# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:38:40 2015

Motor Controller 

@author: anyuser
"""

import numpy
import matplotlib.pyplot as plt
import Utils
import Navigation
import Powertrain
import Motor
import MovementSimulator


"""

Input is TargetHeading
  
   --o--->[NAVIGATION]->[POWERTRAIN]-+->[MotorRight]-+->[MovementSimulator]-+--
     |                               |               |                      |
     |(Subract)                      +->[MotorRight]-+                      |    
     |                                                                      |
     +----------------------------------------------------------------------+
 
     MovementSimulator
         UnitTests DONE & OK
     MotorXXX
         Test with Graphs DONE & OK
     POWERTRAIN 
         UnitTests DONE & OK
     NAVIGATION
         Stub with simple control mechanism
         TODO: PI Controller
    
    
    
""" 

#SETTINGS / PARAMETERS
TARGET_HEADING_s8bit = numpy.int8( Utils.Utils_360_to_s8bit(100))
SIMULATION_TIME_INCREMENT_ms = 100
PLOT_WINDOW_LENGTH_ms = 2000
MOTOR_MAX_SPEED = 100 # Percent




#INIT
simulationTime_ms = 0
timeList_ms = []
targetHeading360List = []
currentHeading360List = []
navigationOutputList = []
currentHeadings8bit = numpy.int8( Utils.Utils_360_to_s8bit(0))
motorLeftCurrentSpeed = 0
motorRightCurrentSpeed = 0


#INIT Plot Stuff
fig = plt.figure(1)
plot1 = fig.add_subplot(221)
data221A_targetHeading360List, = plot1.plot(timeList_ms, targetHeading360List, 'bo')
data221B_currentHeading360List, = plot1.plot(timeList_ms, currentHeading360List, 'r+')
plot2 = fig.add_subplot(222)
data222_navigationOutputList, = plot2.plot(timeList_ms, navigationOutputList, 'ro')
plot2.grid(True)

#plot221.axes.set_xlim([0,100])
plot1.axes.set_ylim([0,360])
plot2.axes.set_ylim([-200,+200])

for i in range(1,5):
    ############################################
    #Perform Calculations

    controlError8bit = TARGET_HEADING_s8bit - currentHeadings8bit
    controlOutput = Navigation.NavigationCtrl_Cyclic(SIMULATION_TIME_INCREMENT_ms, controlError8bit)
    powerTrainOut = Powertrain.Powertrain(controlOutput, MOTOR_MAX_SPEED)
    motorLeftCurrentSpeed = Motor.Motor_Cyclic(SIMULATION_TIME_INCREMENT_ms,motorLeftCurrentSpeed, powerTrainOut[0] )
    motorRightCurrentSpeed = Motor.Motor_Cyclic(SIMULATION_TIME_INCREMENT_ms,motorRightCurrentSpeed, powerTrainOut[1] )
    currentHeadings8bit = MovementSimulator.MovementSimulator(motorLeftCurrentSpeed,motorRightCurrentSpeed,currentHeadings8bit)

    ############################################
    #Do the plotting stuff
    timeList_ms.append(simulationTime_ms)
    
    #   Plot 1: heading target vs actual
    targetHeading360List.append(Utils.Utils_s8bit_to_360(TARGET_HEADING_s8bit))
    data221A_targetHeading360List.set_xdata(timeList_ms[:])
    data221A_targetHeading360List.set_ydata(targetHeading360List[:])
         
    currentHeading360List.append(Utils.Utils_s8bit_to_360(currentHeadings8bit))
    data221B_currentHeading360List.set_xdata(timeList_ms[:])
    data221B_currentHeading360List.set_ydata(currentHeading360List[:])

    if (simulationTime_ms < PLOT_WINDOW_LENGTH_ms):
        plot1.axes.set_xlim([0,PLOT_WINDOW_LENGTH_ms])
        plot2.axes.set_xlim([0,PLOT_WINDOW_LENGTH_ms])
    else:
        temp = simulationTime_ms-PLOT_WINDOW_LENGTH_ms
        temp2 = simulationTime_ms+SIMULATION_TIME_INCREMENT_ms
        plot1.axes.set_xlim([temp,temp2])
        plot2.axes.set_xlim([temp,temp2])
        
    plt.draw()
    #print "turn"

    ############################################
    #Housekeeping
    simulationTime_ms += 100
    #time.sleep(0.01)


    ######################
    # Mess with simulation Parameters