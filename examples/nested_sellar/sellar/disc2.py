# -*- coding: utf-8 -*-
"""
  disc2.py generated by WhatsOpt. 
"""
import numpy as np
from sellar.disc2_base import Disc2Base

class Disc2(Disc2Base):
    """ An OpenMDAO component to encapsulate Disc2 discipline """
		
    def compute(self, inputs, outputs):
        """ Disc2 computation """
    
        z1 = inputs['z'][0]
        z2 = inputs['z'][1]
        y1 = inputs['y1']
        if y1.real < 0.0:
            y1 *= -1
        outputs['y2'] = y1**.5 + z1 + z2 
        
# Reminder: inputs of compute()
#   
#       inputs['y1'] -> shape: (1,), type: Float    
#       inputs['z'] -> shape: (2,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Disc2, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Disc2 """
#   
#       	partials['y2', 'y1'] = np.zeros((1, 1))
#       	partials['y2', 'z'] = np.zeros((1, 2))        
