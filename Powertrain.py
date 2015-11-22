# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:27:12 2015

@author: anyuser
"""




#SETTINGS

"""

Powertrain(headingControl, motorMaxSpeed)

Translates relative target heading control signal to motor Speeds for 
left and right motor


Parameters
----------
heading : int
    Output from Closed Loope Controller [-200 ... +200]
motorMaxSpeed : uint
    Maximum speed the motors are allowed to drive in Percent [0 ... +100]
 
    
    
Returns
-------
List[motorSpeedLeft, motorSpeedRight] : int
    Target Speed for each motor. Each in range of [-100 ... +100]
    
"""  

def Powertrain(headingControl, motorMaxSpeed): 
    
    assert motorMaxSpeed <=  100, "motorMaxSpeed out of allowed Limits"
    assert motorMaxSpeed >=    0, "motorMaxSpeed out of allowed Limits"
    assert headingControl <=  200,       "heading out of allowed Limits"
    assert headingControl >= -200,       "heading out of allowed Limits"
    
   
    headingNormalized = headingControl / 128.0   # Range to [-1 ... 1)
    # Range to [-200 ... 200) for e.g. maxSpeed = 100
    headingWeighted = int(headingNormalized * 2.0 * motorMaxSpeed )
    speedLeft = motorMaxSpeed
    speedRight = motorMaxSpeed
    
    if (headingWeighted > 0):
        #Turn to the right side, so lower speed for right wheel
        speedRight -= headingWeighted
    elif (headingWeighted < 0):
        speedLeft += headingWeighted
        
    if speedRight >= 100:
        speedRight = 100
    elif speedRight <= -100:
        speedRight = -100
        
    if speedLeft >= 100:
        speedLeft = 100
    elif speedLeft <= -100:
        speedLeft = -100
        
        
    assert speedLeft <=  100,        "speedLeft out of allowed Limits"
    assert speedLeft >=  -100,       "speedLeft out of allowed Limits"
    assert speedRight <=  100,        "speedRight out of allowed Limits"
    assert speedRight >=  -100,       "speedRight out of allowed Limits"
    
    return [speedLeft, speedRight]