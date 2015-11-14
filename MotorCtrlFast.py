# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:38:40 2015

Motor Controller 

@author: anyuser
"""

INCR_PER_MS = 0.05



   
def MotorCtrlFast_Cyclic(deltaTime_ms, speed, setSpeed):
   global INCR_PER_MS

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
