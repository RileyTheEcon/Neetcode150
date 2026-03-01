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
def flattenList (xss) :
    return [x for xs in xss for x in xs]
####
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
def twoSum(
    nums: list[int], 
    target: int
    ) -> list[int]:
    ''' Provided list of int and target int, we need to find A, B in list
        such that A+B = target.
        
        Soln Stats
        Runtime     P = 100 %
        Memory      P = 5.09%
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
def isValidParan(
        s: str
    ) -> bool:
    
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
    ''' The commented out solution works sufficiently efficiency. The solution
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
# === Singlely-Linked Lists === #
class ListNode :
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #   end def
####
def printList (node):
    while node is not None:
        print(f"{node.val}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()
####
def list_to_linkedList (regList) :
    ''' Unlike C++, variable assignment does not create a copy of data in 
        memory. It creates a reference to data in memory. So variable
        reassignment does not delete data, but redirects the reference
    '''
    # Empty list err catch
    if len(regList)==0 : return None
    
    # Convert to list of node objects
    regList = [ListNode(x) for x in regList]
    
    # Construct list-header
    head = regList.pop(0)       # `head` now points to node1
    current = head              # `current` now points to node1

    for node in regList : 
        current.next = node     # links node1 to node2, node2 to node3, ...
        current = node          # Redirects `current` to next node
    #   end while
    current.next = None         # Not necessary with our current def of l.list

    return head                 # Recall `head` points to node1
####
def addTwoNumbers(
    l1: Optional[ListNode], 
    l2: Optional[ListNode]
    ) -> Optional[ListNode]:
    ''' You are given two non-empty linked lists representing two non-
        negative integers. The digits are stored in reverse order, and each 
        of their nodes contains a single digit. Add the two numbers and 
        return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, 
        except the number 0 itself.
    
        Here we iteratively unpack both LLs along the same index, save 
        the sum of the two entries as a ListNode object, and take care
        to track the carried 1--where needed. For simplicity sake, we
        convert list of ListNodes to LL in a separate loop.
    
        Soln Stats
        Runtime     P = 71.63 %
        Memory      P =  5.25 %
    '''
    #   Define vars in memory
    c  = 0   # Carry the zero
    l3 = []  # Output list
    
    #
    while (l1 is not None)|(l2 is not None)|(c!=0) :
        # Define session vars
        x1 = 0
        x2 = 0
    
        # Get next valid l1 & l2 entries
        if l1 is not None :
            x1 = l1.val
            l1 = l1.next
        if l2 is not None :
            x2 = l2.val
            l2 = l2.next
        #   end if
    
        #   Calc sum
        x3 = (x1 + x2 + c)%10
        c  = math.floor((x1 + x2 + c)/10)
    
        #   Append to list
        l3.append(ListNode(x3))
    #   end while l1 | l2
    #   Convert list3 to linked-list
    head = l3.pop(0) # set first entry to ll-head
    current = head   # direct `current` to head
    
    for node in l3 : # for each entry in l3
        current.next = node # attach next node to ll
        current = node # redirect `current` to next node
    #   end for
    
    current.next = None # cap end of ll
    return head
####
def mergeTwoLists(
    self, 
    list1: Optional[ListNode], 
    list2: Optional[ListNode]
    ) -> Optional[ListNode]:
    ''' Unstated in prompt, ListNode is singlely-linked list
    '''
    # Define combined list in memory
    list3 = []
    
    # Unpack l.list 1
    while list1 is not None :
        list3.append(list1.val)
        list1 = list1.next
    #   end while
    
    # Unpack l.list 2
    while list2 is not None :
        list3.append(list2.val)
        list2 = list2.next
    #   end while
    
    # Use baked-in sort method
    list3.sort()
    
    # Pass to previously defined function
    linked_list = list_to_linkedList(list3)
    
    return linked_list
####

# === | === #
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




