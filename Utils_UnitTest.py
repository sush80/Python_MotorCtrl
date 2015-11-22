# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:11:00 2015

@author: anyuser
"""

import unittest
import Utils as utils
import numpy as np

class Test_Utils_360_to_s8bit(unittest.TestCase):
    
    def test_0(self):
        self.assertEqual(np.int(0), utils.Utils_360_to_s8bit(0))
    
    def test_1(self):
        self.assertEqual(np.int(0), utils.Utils_360_to_s8bit(360))
    
    def test_2(self):
        self.assertEqual(np.int(-128), utils.Utils_360_to_s8bit(180))
    
    def test_3(self):
        self.assertEqual(np.int(1), utils.Utils_360_to_s8bit(1.40625))
    
    def test_4(self):
        self.assertEqual(np.int(127), utils.Utils_360_to_s8bit(178.59375))
    
    def test_5(self):
        self.assertEqual(np.int(-127), utils.Utils_360_to_s8bit(181.40625))
    
    def test_6(self):
        self.assertEqual(np.int(-1), utils.Utils_360_to_s8bit(358.593))
            
'''
    numpy.int8 |  [0 ... 360]  | [-180 ... 180] 
    -----------+---------------+-----------------
            0  |    0 = 360    |   0
            1  |    1,40625    |   1,40625
         +127  |  178,59375    |   178,59375
         -128  |  180          |   180 = -180
         -127  |  181,40625    |  -178,593
           -1  |  358,59375    |  -1,40625
           '''
 

class Test_Utils_s8bit_to_360(unittest.TestCase):
    
    def test_0(self):
        self.assertEqual(0, utils.Utils_s8bit_to_360(np.int8(0)))  
    
    def test_1(self):
        self.assertEqual(1.40625, utils.Utils_s8bit_to_360(np.int8(1)))  
    
    def test_2(self):
        self.assertEqual(178.59375, utils.Utils_s8bit_to_360(np.int8(127)))  
    
    def test_3(self):
        self.assertEqual(180, utils.Utils_s8bit_to_360(np.int8(-128)))  
    
    def test_4(self):
        self.assertEqual(181.40625, utils.Utils_s8bit_to_360(np.int8(-127))) 
    
    def test_5(self):
        self.assertEqual(358.59375, utils.Utils_s8bit_to_360(np.int8(-1)))           

if __name__ == '__main__':
    
    unittest.main(  )