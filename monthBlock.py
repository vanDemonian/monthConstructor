#!/usr/bin/python
import glob
from PIL import Image
from PIL import ImageStat
from PIL import ImageChops
from PIL import ImageFont
from PIL import ImageDraw
from PIL.ExifTags import TAGS, GPSTAGS
import string, sys, traceback, datetime, time, calendar
import os, shutil
from PIL import *
import math
from monthMaker import *


outputDir = 'Outputs'

#def dayBlock(DAY, blockSize):

def monthBlock(MONTH):

	'Creates a monthBlock from a list of DAY JPGs'

	backGround = (255,255,255)

	"""
	1*4's			x = 1920 * y = 5112

    4*1's 			x = 7680 * y = 1278     
	"""

	imageWidth  = imW = 1920
	imageHeight = imH = 5112

	thumbSize   = (imW, imH)

	# 			 	 width, height
	blockSize1 = (     imW, 31 * imH)  # one column of 31 rows / images
	blockSize2 = (31 * imW,     imH)  # 31 columns of one row / image
	

	blockSize = blockSize2 # which blockSize to use? 1, 2 or 3


	quality = 100


	if os.path.isdir(outputDir) != 1:
            os.mkdir(outputDir)

	cellInfo = []
	monthName = os.path.basename(MONTH[0])
	
	location = monthName[0:7]
	thisMonth = monthName[8:15]
	
	print '\n the month is  ', thisMonth
	print ' '


	#create new Proof.tiff file
	Proofimg = Image.new('RGB', blockSize, backGround)

	
	fnt = ImageFont.truetype('TrueTypeFonts/arial.ttf', 30)

	#process all thumbs from day
	for name in MONTH:

	
		#resize
		img = Image.open(name).resize(thumbSize)
		name = os.path.basename(name)
		#parse cellInfo
		nameInfo = monthMaker(name) # call to cellNUmbers function that delivers info for each image in proof set 
		cellInfo.append(nameInfo) #list of cellInfo for each cell

   		Proofimg.paste(img,(nameInfo[8][0],nameInfo[8][1]))
   		#print "cellInfo = ", nameInfo[8][0],nameInfo[8][1]


   	#Proofimg.save(outputDir+'/'+nameInfo[2] +'_'+ today +'_'+'PROOF_'+'.tif','tiff', quality=quality)#tiff
   	#Proofimg.save(outputDir+'/'+nameInfo[2] +'_'+ today +'_'+'PROOF_'+'.jpg','jpeg', quality =100)#jpeg

   	Proofimg.save(outputDir +'/'+ location + '_' + thisMonth +'_'+'.tif','tiff', quality = quality )#jpeg
	

	print 'cellInfo ', cellInfo




