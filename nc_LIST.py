# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:36:27 2026

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
def flattenList (xss) :
    return [x for xs in xss for x in xs]
####
def maxArea(
        height: list[int]
        ) -> int :
    ''' (#11) CONTAINER WITH THE MOST WATER
        Category: List
        You are given an integer array height of length n. There are n vertical
        lines drawn such that the two endpoints of the ith line are (i, 0) and 
        (i, height[i]).
        Find two lines that together with the x-axis form a container, such 
        that the container contains the most water.
        Return the maximum amount of water a container can store.
        
        Sol'n Stats
        Runtime     %-tile = 42.06 %
        Memory      %-tile = 60.11 %
        O-time      O(n**1)
    '''
    #
    left, right = 0, len(height) - 1
    maxWater   = 0

    #
    while left < right :
        # Calc water for current window
        width = right - left
        currentWater = min(height[left], height[right]) * width
        maxWater = max(maxWater, currentWater)

        # Move the pointer with the shorter side
        if height[left] < height[right] :
            left += 1
        else :
            right -= 1
        #   end if
    #   end width

    return maxWater
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




