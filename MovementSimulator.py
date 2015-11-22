# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:27:12 2015

@author: anyuser
"""

import numpy



#SETTINGS
WEIGHT_DIRECTION_CHANGE = 20

def DEBUG_SET_WEIGHT_DIRECTION_CHANGE(val):
    global WEIGHT_DIRECTION_CHANGE    
    WEIGHT_DIRECTION_CHANGE = val    

"""

MovementSimulator(motorLeft, motorRight, s8bit_currentHeading)

Stub Simulator of Motor driven System. Takes input from controller, returns 
simulated heading


Parameters
----------
motorLeft : int
    Input to drive Motors [-100 ... +100]
motorRight : int
    Input to drive Motors [-100 ... +100]
s8bit_currentHeading : numpy.int8
    Heading [-128 ... +127]
 
    
    
Returns
-------
numpy.int8 : Direction_s8bit
    Simulated heading [-128 ... +127]
    
"""  

def MovementSimulator(motorLeft, motorRight, currentHeading):
    global WEIGHT_DIRECTION_CHANGE    
    
    assert motorLeft <=  100, "motorLeft out of allowed Limits"
    assert motorLeft >= -100, "motorLeft out of allowed Limits"
    assert motorRight <=  100, "motorRight out of allowed Limits"
    assert motorRight >= -100, "motorRight out of allowed Limits"
    assert currentHeading <=  127,       "heading out of allowed Limits"
    assert currentHeading >= -128,       "heading out of allowed Limits"
    assert type(currentHeading) is  numpy.int8
   
    delta = motorLeft - motorRight
    delta = delta / 200.0  #Scale to [-1 ... 1]

    assert delta <=  1
    assert delta >= -1
    
    weightedDelta = delta * WEIGHT_DIRECTION_CHANGE
    ret=  currentHeading
    
    #if delta > 0: 
        #motorLeft > motorRight : Driving to right side
    #   ret = currentHeading + np.int8(weightedDelta)
    #elif delta < 0: 
    #    ret = currentHeading + np.int8(weightedDelta)
    ret = currentHeading + numpy.int8(weightedDelta)
        
        
    assert ret <=  127,       "heading out of allowed Limits"
    assert ret >= -128,       "heading out of allowed Limits"
    return ret
    
    #FIXME Driving to one side needs weighting with delta