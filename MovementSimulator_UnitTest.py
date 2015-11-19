# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:07:29 2015

@author: anyuser
"""


#def Powertrain(heading, motorMaxSpeed): 

import unittest
import MovementSimulator as mvSim
import numpy as np

class Test_Basics(unittest.TestCase):
    
    def test_0(self):
        with self.assertRaises(AssertionError):
            mvSim.MovementSimulator(101,0,np.int8(0))
            
    def test_1(self):
        with self.assertRaises(AssertionError):
            mvSim.MovementSimulator(0,101,np.int8(0))
            
    def test_2(self):
        with self.assertRaises(AssertionError):
            mvSim.MovementSimulator(0,0,128)
            
    def test_3(self):
        with self.assertRaises(AssertionError):
            mvSim.MovementSimulator(0,0,-129)
            
    def test_4(self):
        with self.assertRaises(AssertionError):
            mvSim.MovementSimulator(-101,0,np.int8(0))
            
    def test_5(self):
        with self.assertRaises(AssertionError):
            mvSim.MovementSimulator(0,-101,np.int8(0))
            
    def test_6(self):
        ret = mvSim.MovementSimulator(0,0,np.int8(0))
        self.assertEqual(ret,0)   
            
    def test_7(self):
        ret = mvSim.MovementSimulator(100,0,np.int8(0))
        self.assertEqual(ret,5) 
            
    def test_8(self):
        ret = mvSim.MovementSimulator(0,100,np.int8(0))
        self.assertEqual(ret,-5)  
            
    def test_9(self):
        ret = mvSim.MovementSimulator(100,0,np.int8(-10))
        self.assertEqual(ret,-5) 
            
    def test_10(self):
        ret = mvSim.MovementSimulator(0,100,np.int8(20))
        self.assertEqual(ret,15)    
   
     #   self.assertEqual(ret[1],-98) #due to datatype limitations
            
            

if __name__ == '__main__':
    
    unittest.main(  )