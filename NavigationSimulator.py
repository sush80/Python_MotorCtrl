# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:27:12 2015

@author: anyuser
"""

import numpy as np

"""

NavigationSimulator(controlInput, s8bit_currentHeading)

Stub Simulator of Motor System. Takes input from controller, returns 
simulatied heading


Parameters
----------
controlInput : int
    Input to drive Motors [-200 ... +200]
s8bit_currentHeading : numpy.int8
    Heading [-128 ... +127]
 
    
    
Returns
-------
numpy.int8 : Direction_s8bit
    Simulated heading [-128 ... +127]
    
"""  

def NavigationSimulator(controlInput, s8bit_currentHeading):
    
    if controlInput > 0:
        return s8bit_currentHeading + np.int8(1)
    elif controlInput < 0:
        return s8bit_currentHeading - np.int8(-1)
    return np.int8(0)
    
    #shall include left and right motor ??