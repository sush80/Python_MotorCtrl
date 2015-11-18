# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:27:12 2015

@author: anyuser
"""



"""

MotorCtrl_SystemSensorStub(controlInput)

Stub Simulator of Motor System. Takes input from controller, returns 
simulatied heading


Parameters
----------
controlInput : int
    Input to drive Motors [-200 ... +200]
 
    
    
Returns
-------
uint: Direction_s8bit
    Simulated heading [-128 ... +127]
    
"""  

def MotorCtrl_SystemSensorStub(controlInput, s8bit_currentHeading):
    
    if controlInput > 0:
        return s8bit_currentHeading + 1
    elif controlInput < 0:
        return s8bit_currentHeading - 1
    return 0
    