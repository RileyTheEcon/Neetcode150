# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:42:00 2026

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
class ListNode :
    ''' Create Singlely linked list object
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #   end def
####
def printList (node):
    ''' (Helper function)
    '''
    while node is not None:
        print(f"{node.val}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()
####
def list_to_linkedList (regList) :
    ''' (Helper function)
        Unlike C++, variable assignment does not create a copy of data in 
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
def mergeTwoLists(
    list1: Optional[ListNode], 
    list2: Optional[ListNode]
    ) -> Optional[ListNode]:
    ''' (#21) MERGE TWO SORTED LISTS
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted list. The list should be made by 
        splicing together the nodes of the first two lists.
        Return the head of the merged linked list.
        
        Sol'n Stats
        Runtime     %-tile = 13.77 %
        Memory      %-tile =  5.86 %
        O-time      O[(n+m)*log(n+m)] #can be improved
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
def addTwoNumbers(
    l1: Optional[ListNode], 
    l2: Optional[ListNode]
    ) -> Optional[ListNode]:
    ''' (#2) ADD TWO NUMBERS
        You are given two non-empty linked lists representing two non-
        negative integers. The digits are stored in reverse order, and each 
        of their nodes contains a single digit. Add the two numbers and 
        return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, 
        except the number 0 itself.
    
        Here we iteratively unpack both LLs along the same index, save 
        the sum of the two entries as a ListNode object, and take care
        to track the carried 1--where needed. For simplicity sake, we
        convert list of ListNodes to LL in a separate loop.
    
        Sol'n Stats
        Runtime     %-tile = 71.63 %
        Memory      %-tile =  5.25 %
        O-time      O[max(m, n)]
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




