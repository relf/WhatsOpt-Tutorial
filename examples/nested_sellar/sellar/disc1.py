# -*- coding: utf-8 -*-
"""
  disc1.py generated by WhatsOpt. 
"""
import numpy as np
from sellar.disc1_base import Disc1Base

class Disc1(Disc1Base):
    """ An OpenMDAO component to encapsulate Disc1 discipline """
		
    def compute(self, inputs, outputs):
        """ Disc1 computation """
    
        z1 = inputs['z'][0]
        z2 = inputs['z'][1]
        x1 = inputs['x']
        y2 = inputs['y2']

        outputs['y1'] = z1**2 + z2 + x1 - 0.2*y2
        
# Reminder: inputs of compute()
#   
#       inputs['x'] -> shape: (1,), type: Float    
#       inputs['y2'] -> shape: (1,), type: Float    
#       inputs['z'] -> shape: (2,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Disc1, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Disc1 """
#   
#       	partials['y1', 'x'] = np.zeros((1, 1))
#       	partials['y1', 'y2'] = np.zeros((1, 1))
#       	partials['y1', 'z'] = np.zeros((1, 2))        
