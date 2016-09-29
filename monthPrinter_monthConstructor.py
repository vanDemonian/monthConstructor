#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------------------------------
Filename:           JPG_monthPrinter.py
Author:             Martin Walch
Release Date:       2016-09-20
Description:        HI-Res month Printer
                    
            ****    No gaps between thumbnails  *****

                    Iterates through a directory tree of JPG's renamed by JPG_reNamer.py.

                    TARONGA_2014_09_29-11_56_58.jpg



            ****    paperSize:   in pixels (width, height)
                    

                    Standard Nikon D3200 File = 4512 x 3000  (width by height)
                    therefore       width     = 1.504 x height
                                    height    = 0.665 x width
                    
                    1920 x 1278
                    
                    OUTPUT VARIABLES

                    Format 1:

                    Format 2:

                    Format 3:
            

Required Modules:  
                    cellData.py
                    proofSheet.py
---------------------------------------------------------------------------------------------------
"""
import glob
from PIL import Image
from PIL import ImageStat
from PIL import ImageChops
from PIL.ExifTags import TAGS, GPSTAGS
import string, sys, traceback, datetime, time, calendar
import os, shutil
from PIL import *
import math
from multiprocessing import Pool
from proofSheet_Multi import *
from monthMaker import *
from monthBlock import *



inputDir = '/Volumes/3TB_DP/DTLA_12_Station_Proofs/1x4s'   #root directory that will be parsed (includes subdirectories)
#outputDir = '/Users/pyDev/Documents/JPG_dayProofer_Multi/JPG_proof_Outputs' #output directory (must be created before script is run)
fileExt = '.tif'
#cameraInterval = 300 #this is the number of seconds between each capture:   5mins = 300 secs

nameList = []
namePathList = []
namePathList_Filtered = []
monthList = []
cellInfo = []

MonthChangeList =[]

MONTHS = []
count = 0



def Timer(start, end):
    """
    Calculates the time it takes to run a process, based on start and finish times
    ---------------------------------------------------------------------------------------------
    Inputs:       in seconds 
    start:        Start time of process
    end:          End time of process
    ---------------------------------------------------------------------------------------------
    """
    elapsed = end - start
    # Convert process time, if needed
    if elapsed <= 59:
        time = str(round(elapsed,2)) + " seconds\n"
    if elapsed >= 60 and elapsed <= 3590:
        min = elapsed / 60
        time = str(round(min,2)) + " minutes\n"
    if elapsed >= 3600:
        hour = elapsed / 3600
        time = str(round(hour,2)) + " hours\n"
    return time


##### RUN #####

if __name__ == '__main__':
    #start = time.clock()
    start = time.time()

    print '   '
    print 'JPG_monthPrinter_monthConstructor.py   '
    print '   '

    # loop to create list of names and paths
    for root, dirs, files in os.walk(inputDir):
        for name in files:
            
            if name.endswith(fileExt):

                nameList.append(name)           #list of filenames - basename only
                namePathList.append(os.path.join(root,name))    #list of names with directory paths

                count = count + 1

    #---------------------------------------------------------------
    #print namePathList - debug

    #set date of first name as today and appends it to the start of 'monthList'
    todaysMonth = nameList[0][8:15]
    monthList.append(todaysMonth)
    print "monthList Start  ", monthList # - debug

    #   loop to create list of MONTHS by checking if the date changes
    #   and adding the date to the list of dates it does.
    for name in nameList:

        if name[8:15] != todaysMonth:
            #create new day and append name
            monthList.append(name[8:15])
            #make the new date = 'today'
            todaysMonth = name[8:15]


    numberofMONTHS = len(monthList)
    print 'Number of MONTHS = ', numberofMONTHS


    #---------------------------------------------------------------
    print "________________________________________________________"

    #for name in namePathList:
    #   print name

    print "________________________________________________________"
    print "________________________________________________________"
    #---------------------------------------------------------------

    today = 0

    for i in range(len(namePathList)):
        month = os.path.basename(namePathList[i])

        month = month[8:15]
        #print month
        if month != today:
            today = month
            MonthChangeList.append(i)
        
        print ' ', i, '   ', month

    MonthChangeList.append(len(namePathList))
    print 'Month Change List  ', MonthChangeList


    #---------------------------------------------------------------

    d = 0

    for x in range(len(MonthChangeList)-1):
        #print x,' ', len(namePathList)
        v = MonthChangeList[d]
        
        v1 = MonthChangeList[(d+1)]
        print 'v ',v,'v1 ',v1
        proofPath = namePathList[v:v1]
        print proofPath

        MONTHS.append(proofPath)

        d+=1

    #---------------------------------------------------------------
    print
    print "Months    ", MONTHS[-1]

    #---------------------------------------------------------------




    pool = Pool()
    pool.map(monthBlock, MONTHS)
    pool.close()
    pool.join()

    print ' '
    print ' '
    print ' '

   




    finish = time.time()



    print 'List of Months in data', monthList
    print 'Total Number of Months = ', len(monthList)
    print 'Total Number of Images processed: ', str(count)
    print 'Processing done in ', Timer(start, finish), '\n'






