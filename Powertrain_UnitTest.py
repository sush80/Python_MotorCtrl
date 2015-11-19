# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:07:29 2015

@author: anyuser
"""


#def Powertrain(heading, motorMaxSpeed): 

import unittest
import Powertrain as powertrain
import numpy as np

class Test_Basics(unittest.TestCase):
    
    def test_0(self):
        with self.assertRaises(AssertionError):
            powertrain.Powertrain(0,101)
            
    def test_1(self):
        with self.assertRaises(AssertionError):
            powertrain.Powertrain(0,-1)
            
    def test_2(self):
        with self.assertRaises(AssertionError):
            powertrain.Powertrain(-129,0)
            
    def test_3(self):
        with self.assertRaises(AssertionError):
            powertrain.Powertrain(+128,0)
            
    def test_4(self):
        ret = powertrain.Powertrain(0,100)
        self.assertEqual(ret[0],100)
        self.assertEqual(ret[1],100)
            
    def test_5(self):
        ret = powertrain.Powertrain(np.int8(128/2),100)
        self.assertEqual(ret[0],100)
        self.assertEqual(ret[1],0)
            
    def test_6(self):
        ret = powertrain.Powertrain(np.int8(-128/2),100)
        self.assertEqual(ret[0],0)
        self.assertEqual(ret[1],100)
            
    def test_7(self):
        ret = powertrain.Powertrain(np.int8(-128),100)
        self.assertEqual(ret[0],-100)
        self.assertEqual(ret[1],100)
            
    def test8(self):
        ret = powertrain.Powertrain(np.int8(+127),100)
        self.assertEqual(ret[0],+100)
        self.assertEqual(ret[1],-98) #due to datatype limitations
            
            

if __name__ == '__main__':
    
    unittest.main(  )