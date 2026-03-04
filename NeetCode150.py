# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 17:27:38 2025

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
# === Basic Data Structures === #
def isHappy(
        n: int
        ) -> bool:
    ''' For a provided integer, return whether it is a "Happy Number"
    
        The solution below is sufficiently efficient. Efficiency can be gained
        by reducing the number of times lists are called.
    '''
    #   Create vars in memory
    memory = []     # break loop if int has been seen before

    while (n!=1)&(n not in memory) :
        #   Add integer-input to memory
        memory.append(n)
        
        #   Convert int to digit-wise list
        digits = [int(d) for d in str(n)]

        #   Calc sums
        n = 0
        for d in digits : n += d**2
    #   end while

    return n==1
####
def lengthOfLongestSubstring(
    s: str
    ) -> int:
    ''' Given a string s, find the length of the longest substring without 
        duplicate characters.
        This is a sliding-window problem. Due to how duplicate letters can
        appear in any pattern in the input, we have to proceed with 
        caution. While an exhaustive check of all substr works, it also
        runs in O^3 time. By taking advantage of info gained thru prev
        iters, we can reduce this to O^1.
        Here, we start by considering a 1-char window at the start of the
        str. If the substr is valid, then the right-bound is moved over
        one. If the substr is invalid, then the left-bound is moved over
        one. Thus if a char/position is a duplicate, we are able to
        continue by considering the substrs that don't include it.
        
        Soln Stats
        Runtime     P = 99.74 %
        Memory      P =  9.09 %
    '''
    #   Define vars in memory
    seen   = set()
    left   = 0
    maxLen = 0
    
    #   Iter by right-bnd index
    for right in range(len(s)) :
        #   If substr invalid, move left-bnd until valid
        while s[right] in seen :
            seen.remove(s[left])
            left += 1
        #   end while
    
        #   Else, move right-bnd by one
        seen.add(s[right])
        maxLen = max(maxLen, right-left+1)
    #   end for
    
    return maxLen
####
def hasDuplicate(
        nums: list[int]
        ) -> bool:
    ''' Assuming we are allowed to use sets
    '''
    return len(nums) != len(set(nums))
####
def singleNumber(
        nums: list[int]
        ) -> int :
    ''' Provided a list of integers in which all but one elem is duplicated,
        return the integer that is not duplicated.
    
        Original solution
        #   Use itertools to extract single list entry
        return [x for x in nums if nums.count(x)==1][0]
    
        The original solution is O(n**2). For every x in nums, nums.count(x) is
        called, which in turn iterated through nums again. The current solution
        runs through nums only once.
        
        This works bc XOR is commutative and associative. So `ret` acts as a
        running logic chain in which all duplicated elem will cancel, leaving
        just the singleton.
    '''
    ret = nums[0]
    for num in nums[1:]:
        ret = (ret ^ num)
    return ret
####
def plusOne(
        digits: list[int]
        ) -> list[int]:
    #   Get input stats
    carry    = 0
    digitLen = len(digits)
    position = digitLen - 1     # shift for Py indexing

    #   Increment ones-space
    x = digits[position] + 1

    digits[position] = x%10     # assign ones place
    carry = math.floor(x/10)    # get carried one

    #   Iter for carried values
    while (carry > 0)&(position > 0) :
        position -= 1   # decrement index

        # Calc new value
        x = digits[position] + 1

        digits[position] = x%10     # assign ones place
        carry = math.floor(x/10)    # get carried one

    #   end while

    #   Additional place
    if carry > 0 : digits = [1] + digits
    
    return digits
####
# ===        Binary         === #
''' Assuming we cannot use `bin(x)` to simplify these operations and so have to
    work around needing to also convert integers to bits
'''
def hammingWeight(
        n: int
        ) -> int:
    ''' The commented out solution works sufficiently efficienct. The solution
        below is one of the canonical solutions for this problem.
    
    #   Create vars in memory
    ones = 0
    twos = [2**(31-i) for i in range(32)]


    #   Iter thru 32-bits, descending
    for i in range(32) :
        if n >= twos[i] :
            n -= twos[i]
            ones += 1
        #   end if
    #   end for
    '''
    #   Create var in memory
    ones = 0 
    
    #   While n not 0, flip bits
    while n :
        n = n & (n-1)
        ones += 1
    #   end while

    return ones
####
def reverseBits(
        n: int
    ) -> int:
    ''' Provided an integer, convert to a binary string, reverse the 
        string, convert back to integer and return.

        Soln Stats
        Runtime     P = 30.89 %
        Memory      P =  7.07 %
    '''
    #   Create vars in memory
    y    = 0
    twos = [2**(31-i) for i in range(32)]

    #   Iter thru 32-bits
    for i in range(32) :
        if n >= twos[i] :
            n -= twos[i]   # remove larges 2-power
            y += 2**i      # add the reverse to output
        #   end if
    #   end for

    return y
####
# === MAIN === #
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




