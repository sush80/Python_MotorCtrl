# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:10:40 2015

@author: anyuser
"""

import numpy


"""
Utils_360_to_s8bit(input360)

Transformation from angles in range of [0 ... 360] to signed 8bit Datatype
[-128 ... 127]

    numpy.int8 |  [0 ... 360]  | [-180 ... 180] 
    -----------+---------------+-----------------
            0  |    0 = 360    |     0
            1  |    1.40625    |     1.40625
         +127  |  178.59375    |   178.59375
         -128  |  180          |   180 = -180
         -127  |  181.40625    |  -178.593
           -1  |  358.59375    |    -1.40625

Parameters
----------
input360 : int
    Degree [0 ... 360]
    
    
Returns
-------
numpy.int8 
    Transformed angle [-128 ... 127]
    
""" 
def Utils_360_to_s8bit(input360):
    assert input360 >= 0,   "Input out of Range"
    assert input360 <= 360, "Input out of Range"
    
    #[0 ...360] -> [-180 ... 180]
    if input360 > 180:
        temp =  input360 - 360
    else:
        temp = input360
    
    #[-180 ... 180] -> [-1 ... +1]
    temp = temp / 180.0
    
    #[-1 ... +1] -> [-128 ... +128]
    temp *= 128
    
    temp = int(temp)
    
    #+128 will be transformed to -127 here if needed.
    result = numpy.int8(temp)
    return result
    
''' 
Vice versa to Utils_360_to_s8bit

Parameters
----------
inputs8bit : numpy.int8
    angle [-128 ... 127]
    
    
Returns
-------
float
    Degree [0 ... 360]
''' 
def Utils_s8bit_to_360(inputs8bit):
    assert type(inputs8bit) is  numpy.int8
    
    #[-128 ... +127] -> [-1 ... +1)
    temp = inputs8bit / 128.0
    
    #[-1 ... +1) -> [-180 ... 180)
    temp *= 180.0
    
    #[-180 ... 180) -> [0 ...360)
    if (temp < 0):
        temp += 360.0

    return temp
    