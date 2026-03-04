# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:30:36 2026

@author: RC
"""





# ================================ LIBRARIES ================================ #
# import sys
# if sys.prefix[sys.prefix.rindex('\\')+1:] == 'geoSpyder' :
#     sys.path.append('C:\\Users\\conlon\\Anaconda3\\Lib')
# #   endif

import os
import time
import math
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional
# import RileysLibrary
#

dictIn = {'dictIn' : 'place_holder'}

# =========================================================================== #





# ================================ FUNCTIONS ================================ #
def twoSum(
    nums: list[int], 
    target: int
    ) -> list[int]:
    ''' (#1) Two Sum
        Category: INT
        Provided list of int and target int, we need to find A, B in list
        such that A+B = target.
        
        Sol'n. Stats
        Runtime     P = 100 %
        Memory      P = 5.09%
        O-time      O(n**1)
    '''
    dictMem = {} # create memory dictionary

    # Iter thru list of nums
    for i, num in enumerate(nums) :
        # Assuming num is B, then target - B = A (= comp)
        comp = target - num

        # Check if potential A is in memory
        ## We cannot check nums directly bc it causes errs when num*2=target
        if comp in dictMem :
            return [i, dictMem[comp]]
        #   end if
        # Save observed num, index to memory
        dictMem[num] = i
    #   end for
####

def main (dictIn) :
    
    pass
#   end 
# =========================================================================== #





# =================================== MAIN ================================== #
if __name__ == "__main__" :
    print(__doc__)
    
    main(**dictIn)
    
#   endif
# =========================================================================== #




