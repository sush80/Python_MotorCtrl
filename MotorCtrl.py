# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:38:40 2015

Motor Controller 

@author: anyuser
"""

INCR_PER_MS = 0.05



"""
MotorCtrlFast_Cyclic(deltaTime_ms, speed, setSpeed)

Control ramping for Motor Control to desired target setSpeed.
Call in regular Intervalls

Parameters
----------
deltaTime_ms : uint32
    Time in Milliseconds since last kall of Cyclic Function
speed : uint32
    current speed [-100 ... +100]
setSpeed : uint32
    target speed [-100 ... +100]
    
    
Returns
-------
uint
    new Speed
    
""" 
def MotorCtrlFast_Cyclic(deltaTime_ms, speed, setSpeed):
   global INCR_PER_MS

   assert speed <=  100, "speed out of allowed Limits"
   assert speed >= -100, "speed out of allowed Limits"
   assert setSpeed <=  100, "setSpeed out of allowed Limits"
   assert setSpeed >= -100, "setSpeed out of allowed Limits"

   if(speed > 100):
       print
       return 0
      
   INCR = INCR_PER_MS * deltaTime_ms
   retVal = setSpeed
   if (speed > setSpeed):
      retVal = speed - INCR 
   if (speed < setSpeed):
      retVal = speed + INCR 
   
   #Limiters
   if (retVal > 100):
       return 100
   if (retVal < -100):
       return -100

   return retVal
