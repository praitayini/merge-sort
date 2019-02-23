#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:56:23 2017

@author: praitayinikanakaraj
"""
#To import all the required library
import os  #for miscellaneous operating system interfaces
import re  #for regular expression operation
import json #for JSON encoding and decoding 

contents =[];
lines = [];

#PART 1: Reading text content into files
def readFile(path): #takes the location of a file as input
    for i in range(0,len(path)):           #means until all the path (.txt files) is considered
        with open(path[i], mode='r') as f: #to open the file in read mode
            f_contents=f.read();           #reads the file 
            contents.append(f_contents);   #stores the contents of the file in list 'contents'. Each list 'contents'
                                           #contains the entire file as a string 
            l = contents[i].split('\n')    #splits each line in the content and stores in l
            print "***********"
            print l                        #prints out the file we read
            
patients = []
path =[];  
#PART 2 Extracting useful information from the string in the contents
def fileSearch(): 
    for i in range(0,len(path)):           #means until all the path (.txt files) is considered
        dictonary={};                      
        
        pi = re.search(r'TCGA.+?(?=\.t)',path[i])  #uses regular expressions to search for the patient id
        if pi== None:                              #if it is not found
            dictonary["PATIENT ID"]= "_NA_"        #then it is assigned to "_NA_" to indicate it is not avaliable
        else:                                      #if found
            api = pi.group(0)                      #extracts the patient id and stores it in variable
            dictonary["PATIENT ID"] = api          #maps the extracted to a dictonary to have key-value pair
            
        #similar apporach is used to extract other four information - pathological diagnosis, gross pathology
        #microscopic and intraoperative consulation
            
        pa = re.search(r'PATHOLOGI(.*)\n(.*)\n',contents[i])
        if pa == None:
            dictonary["PATHOLOGICAL DIAGNOSIS"]= "_NA_"
        else:
            ap = pa.group(0)
            dictonary["PATHOLOGICAL DIAGNOSIS"] = ap.replace('PATHOLOGICAL DIAGNOSIS:',"").replace("\n","")
                
        g = re.search(r'GROSS(.*)\n(.*)\n',contents[i])
        if g == None:
            dictonary["GROSS PATHOLOGY"]= "_NA_"
        else:
            ag = g.group(0)
            dictonary["GROSS PATHOLOGY"] = ag.replace('GROSS PATHOLOGY:','').replace("\n",'')
            
        m = re.search(r'MICROSCOP(.*)\n(.*)\n',contents[i])
        if m == None:
            dictonary["MICROSCOPIC"]= "_NA_"
        else:
            am = m.group(0)
            dictonary["MICROSCOPIC"] = am.replace('MICROSCOPIC:',"").replace("\n","")
            
            
        ic = re.search(r'INTRA(.*)\n(.*)\n',contents[i])
        if ic == None:
            dictonary["INTRAOPERATIVE CONSULTATION"]= "_NA_"
        else:
            ai = ic.group(0)
            dictonary["INTRAOPERATIVE CONSULTATION"] = ai.replace('INTRAOPERATIVE CONSULTATION:',"").replace("\n","")
        
            patients.append(dictonary)  #stores the patient information in a list called 'patients'.
                                        #each element in the list is the Map of one patient
    return patients                     #returns this list with the dictornaries

#PART 1, PART 2, PART 3, PART 4       
def getFile(location):  #takes the location of the directory
    for file in os.listdir(location):   #to access everything that is in location of the directory
        if file.endswith(".txt"):       #we need only .txt files
            p = os.path.join(location, file)  #to get only the files
            path.append(p)              #make a list of .txt files
            print path                  #prints the list of .txt files
        else:
            print "No text file found"  #to handle cases when there are no .txt files found
    readFile(path)                      #call the function to read the file with the input as the path
                                        #which the list of .txt files obtained from the above lines of code
    patientslist = fileSearch()         #to assign the patient list from the fileSearch function to a variable
    print "The patient list with dictonary (unsorted)"
    print patientslist                  #prints out the list with dictornaties of the patients
    from mysort1 import mergeSort       #to import the mergesort function from mysort1
    print "Importing merge sort"
    print "After merging, The patient list (sorted) is:"
    mergeSort = mergeSort(patientslist,"increasing")  #takes patientslist as the collection to be sorted and does
                                                      #incresing order
    print mergeSort                     #prints the sorted list, sorts it using the patient id
    with open('patientCollection.json','w') as f:     #write a json file
        json.dump(mergeSort,f)          #export the sorted patients list into a JSON file
   


getFile("/Users/praitayinikanakaraj/Desktop")  


