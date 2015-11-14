# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:38:40 2015

Motor PI Controller 

@author: anyuser
"""

P = 0
I = 0
P_Cnt = 0
I_Cnt = 0



def MotorCtrlFast_Init():
   P = 1
   I = 0
   P_Cnt = 0
   I_Cnt = 0
   
   
def MotorCtrlFast_Cyclic(deltaTime_ms, speed, setSpeed):
   
   return speed + 1
