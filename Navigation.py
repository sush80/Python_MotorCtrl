# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 19:38:40 2015

Motor Controller 

@author: anyuser
"""

import numpy

'''
def NavigationCtrl_Init():
    # ???
    return 0
'''

"""
NavigationCtrl_Cyclic(deltaTime_ms, deltaDirection_s8bit)

Closed Loop Controller for Navigation. Input is a signed tow complement number,
allowing the Controller to overcome the nonlinearity issue on the step from
360degree to 0 degree, because the signed 8 bit runs in circles.

Parameters
----------
deltaDirection_s8bit : numpy.int8
    Direction error represented in signed 8 bit. 
    numpy.int8 |  Degree
    -----------+----------------
         -128  | -180 
            0  |    0
            1  |    1,40625
         +127  |  178,59375
 
    
    
Returns
-------
uint
    Output of Controller Limited to [-200 ... +200]
    
"""  
def NavigationCtrl_Cyclic(deltaTime_ms, deltaDirection_s8bit):
#P Ctrl
#  y = Kp * e
#I Ctrl
#  esum = esum + e
#  y = Ki * Ta * esum
   
 
   assert type(deltaDirection_s8bit) is  numpy.int8   
   
   return deltaDirection_s8bit
   '''
    
   if deltaDirection_s8bit > 0:
       return 1
   elif deltaDirection_s8bit < 0:
       return -1
   return 0
   '''
   
   #Limit to [-200 ... +200]
   
   