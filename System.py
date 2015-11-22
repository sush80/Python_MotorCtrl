# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:38:40 2015

Motor Controller 

@author: anyuser
"""

import numpy



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
TARGET_HEADING_360 = 100


TARGET_HEADING_s8bit = 



