#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:02:17 2017

@author: praitayinikanakaraj
"""

#PART 3 Merge Sort algorithm
def mergeIncrease(sorted_l,sorted_r): #this function takes sorted rigth and left array
    d =[];
    i=0;
    j=0;
    while i<len(sorted_l) and j<len(sorted_r):
        if sorted_l[i] > sorted_r[j]:  #compares one element in both array one at a time 
                                       #if the number in the left array is high
            d.append(sorted_l[i]);     #then we push it into a new array (the sorted one - here it is d)
            i = i + 1                  #we iterate i so we the do the above process for the rest of elements in left array
        else:
            d.append(sorted_r[j])      #push the number in the right to new array, as it is higher that the number
                                       #in the left array
            j = j + 1                  #we iterate j so we the do the above process for the rest of elements in right array
    #there might be some elements remaining in the either one of the array
    #we push these remaining elements in the sorted array and return it
    remainleft=sorted_l[i:]
    remainright=sorted_r[j:]
    d = d + remainleft
    d = d + remainright
    return d

#similar is done for decreasing
def mergeDecrease(sorted_l,sorted_r): 
    d =[];
    i=0;
    j=0;
    while i<len(sorted_l) and j<len(sorted_r):
        if sorted_l[i] < sorted_r[j]:
            d.append(sorted_l[i]); 
            i = i + 1
        else:
            d.append(sorted_r[j])
            j = j + 1
    remainleft=sorted_l[i:]
    remainright=sorted_r[j:]
    d = d + remainleft
    d = d + remainright
    return d 


def mergeSort(collection,order): #main function that inputs the list of numbers and the order to be sorted
    if(len(collection) <= 1):    #if the list of numbers is less than 1 we dont have perform sorting
        return collection        #and the sorting is stopped and the sorted list is returned
    else:
        mid = len(collection)/2                                #if the list has more than 2 elements we divide it
        l = mergeSort(collection[0:mid],order)                 #and call the same function on each half
        r = mergeSort(collection[mid:len(collection)],order)   #this happens until we has one element in each array
        if order == "increasing":
            return mergeIncrease(l,r) #the right and left from the above recursion is given to merge, to merge the array
        else:
            return mergeDecrease(l,r)
    




    
