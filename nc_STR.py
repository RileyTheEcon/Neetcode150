# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:33:09 2026

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
def isValidParan(
        s: str
    ) -> bool :
    ''' (#20) Valid Parantheses
        Category: STR
        Given a string s containing just the characters 
        '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
        1) Open brackets must be closed by the same type of brackets.
        2) Open brackets must be closed in the correct order.
        3) Every close bracket has a corresponding open bracket of the same type.
        
        Sol'n. Stats
        Runtime     P = 4.13%
        Memory      P = 100 %
        O-time      O(n**1)
    '''
    
    # Def memory list
    bValid  = True
    listMem = []
    
    # Iter thru input; append open to memory, remove close, end if invalid
    for item in [*s] :
        if item in ['(','[','{'] : listMem.append(item)
        elif len(listMem)>0 :
            if (item==')')&(listMem[-1]=='(') : listMem.pop()
            elif (item==']')&(listMem[-1]=='[') : listMem.pop()
            elif (item=='}')&(listMem[-1]=='{') : listMem.pop()
            else : bValid = False
        else :
            bValid = False
            break
        #   endif
    
    #   endfor
    if len(listMem)>0: bValid = False
    return bValid
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




