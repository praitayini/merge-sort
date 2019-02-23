#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:27:31 2017

@author: praitayinikanakaraj
"""

from mysort1 import mergeSort      #to import the mergeSort function from mysort1

def testMergeSort():              
    #three test cases
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20];
    print "unsorted array a =", a;
    b = [34, 54, 76, 2, 6, 65, 41, 9, 25, 4];
    print "unsorted array b =", b;
    c = ['a', 'd', 'g', 'h', 'l', 'm', 'k', 'r', 'c', 'h'];
    print "unsorted array c =", c;
    print ""
    print 'Sorting array a in increasing order'
    print(mergeSort(a,"increasing")) #sort number in incresing order
    print 'Sorting array b in decreasing order'    
    print(mergeSort(b,"decreasing")) #sort number in decresing order
    print 'Sorting array c'
    print(mergeSort(c,"decreasing"))  #sort strings in alphabetical order

testMergeSort()
