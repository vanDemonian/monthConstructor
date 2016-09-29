#!/usr/bin/python

def monthMaker(name):
	"""
	creates an individual array representation of the
	31 jpegs for the month

	                Format 1: 1 x 31

                    Format 2: 31 x 1
                    
    1*4's			x = 1920 * y = 5112

    4*1's 			x = 7680 * y = 1278     

	"""
	

	xstep = 1920
	
	ystep = 5112



	location = str(name[0:7])

	print " location  ", location

	date = 		str(name[8:18])
	print " date      ", date

	year = 		int(name[8:12])
	print " year      ", year

	month = 	int(name[13:15])
	print " month     ", month

	day = 		int(name[16:18])
	print " day       ", day



	if   day == 1:
		gridNum = 0
	elif day == 2:
		gridNum = 1
	elif day == 3:
		gridNum = 2
	elif day == 4:
		gridNum = 3
	elif day == 5:
		gridNum = 4
	elif day == 6:
		gridNum = 5
	elif day == 7:
		gridNum = 6
	elif day == 8:
		gridNum = 7
	elif day == 9:
		gridNum = 8
	elif day == 10:
		gridNum = 9

	elif day == 11:
		gridNum = 10
	elif day == 12:
		gridNum = 11
	elif day == 13:
		gridNum = 12
	elif day == 14:
		gridNum = 13
	elif day == 15:
		gridNum = 14
	elif day == 16:
		gridNum = 15
	elif day == 17:
		gridNum = 16
	elif day == 18:
		gridNum = 17
	elif day == 19:
		gridNum = 18
	elif day == 20:
		gridNum = 19

	elif day == 21:
		gridNum = 20
	elif day == 22:
		gridNum = 21
	elif day == 23:
		gridNum = 22
	elif day == 24:
		gridNum = 23
	elif day == 25:
		gridNum = 24
	elif day == 26:
		gridNum = 25
	elif day == 27:
		gridNum = 26
	elif day == 28:
		gridNum = 27
	elif day == 29:
		gridNum = 28
	elif day == 30:
		gridNum = 29
	elif day == 31:
		gridNum = 30


	# 31 columns of one row

	if gridNum == 0:
		cellCoordinates = (0*xstep, 0*ystep)
	if gridNum == 1:
		cellCoordinates = (1*xstep, 0*ystep)
	if gridNum == 2:
		cellCoordinates = (2*xstep, 0*ystep)
	if gridNum == 3:
		cellCoordinates = (3*xstep, 0*ystep)
	if gridNum == 4:
		cellCoordinates = (4*xstep, 0*ystep)
	if gridNum == 5:
		cellCoordinates = (5*xstep, 0*ystep)
	if gridNum == 6:
		cellCoordinates = (6*xstep, 0*ystep)
	if gridNum == 7:
		cellCoordinates = (7*xstep, 0*ystep)
	if gridNum == 8:
		cellCoordinates = (8*xstep, 0*ystep)
	if gridNum == 9:
		cellCoordinates = (9*xstep, 0*ystep)
	if gridNum == 10:
		cellCoordinates = (10*xstep, 0*ystep)
	if gridNum == 11:
		cellCoordinates = (11*xstep, 0*ystep)


	if gridNum == 12:
		cellCoordinates = (12*xstep, 0*ystep)
	if gridNum == 13:
		cellCoordinates = (13*xstep, 0*ystep)
	if gridNum == 14:
		cellCoordinates = (14*xstep, 0*ystep)
	if gridNum == 15:
		cellCoordinates = (15*xstep, 0*ystep)
	if gridNum == 16:
		cellCoordinates = (16*xstep, 0*ystep)
	if gridNum == 17:
		cellCoordinates = (17*xstep, 0*ystep)
	if gridNum == 18:
		cellCoordinates = (18*xstep, 0*ystep)
	if gridNum == 19:
		cellCoordinates = (19*xstep, 0*ystep)
	if gridNum == 20:
		cellCoordinates = (20*xstep, 0*ystep)
	if gridNum == 21:
		cellCoordinates = (21*xstep, 0*ystep)
	if gridNum == 22:
		cellCoordinates = (22*xstep, 0*ystep)
	if gridNum == 23:
		cellCoordinates = (23*xstep, 0*ystep)

	if gridNum == 24:
		cellCoordinates = (24*xstep, 0*ystep)
	if gridNum == 25:
		cellCoordinates = (25*xstep, 0*ystep)
	if gridNum == 26:
		cellCoordinates = (26*xstep, 0*ystep)
	if gridNum == 27:
		cellCoordinates = (27*xstep, 0*ystep)
	if gridNum == 28:
		cellCoordinates = (28*xstep, 0*ystep)
	if gridNum == 29:
		cellCoordinates = (29*xstep, 0*ystep)
	if gridNum == 30:
		cellCoordinates = (30*xstep, 0*ystep)
	

	return  gridNum, location, year, month, day, date, xstep, ystep, cellCoordinates




"""
# 1 column of 31 rows	
	if gridNum == 0:
		cellCoordinates = (0*xstep, 0*ystep)
	if gridNum == 1:
		cellCoordinates = (0*xstep, 1*ystep)
	if gridNum == 2:
		cellCoordinates = (0*xstep, 2*ystep)
	if gridNum == 3:
		cellCoordinates = (0*xstep, 3*ystep)
	if gridNum == 4:
		cellCoordinates = (0*xstep, 4*ystep)
	if gridNum == 5:
		cellCoordinates = (0*xstep, 5*ystep)
	if gridNum == 6:
		cellCoordinates = (0*xstep, 6*ystep)
	if gridNum == 7:
		cellCoordinates = (0*xstep, 7*ystep)
	if gridNum == 8:
		cellCoordinates = (0*xstep, 8*ystep)
	if gridNum == 9:
		cellCoordinates = (0*xstep, 9*ystep)
	if gridNum == 10:
		cellCoordinates = (0*xstep, 10*ystep)
	if gridNum == 11:
		cellCoordinates = (0*xstep, 11*ystep)

	if gridNum == 12:
		cellCoordinates = (0*xstep, 12*ystep)
	if gridNum == 13:
		cellCoordinates = (0*xstep, 13*ystep)
	if gridNum == 14:
		cellCoordinates = (0*xstep, 14*ystep)
	if gridNum == 15:
		cellCoordinates = (0*xstep, 15*ystep)
	if gridNum == 16:
		cellCoordinates = (0*xstep, 16*ystep)
	if gridNum == 17:
		cellCoordinates = (0*xstep, 17*ystep)
	if gridNum == 18:
		cellCoordinates = (0*xstep, 18*ystep)
	if gridNum == 19:
		cellCoordinates = (0*xstep, 19*ystep)
	if gridNum == 20:
		cellCoordinates = (0*xstep, 20*ystep)
	if gridNum == 21:
		cellCoordinates = (0*xstep, 21*ystep)
	if gridNum == 22:
		cellCoordinates = (0*xstep, 22*ystep)
	if gridNum == 23:
		cellCoordinates = (0*xstep, 23*ystep)

	if gridNum == 24:
		cellCoordinates = (0*xstep, 24*ystep)
	if gridNum == 25:
		cellCoordinates = (0*xstep, 25*ystep)
	if gridNum == 26:
		cellCoordinates = (0*xstep, 26*ystep)
	if gridNum == 27:
		cellCoordinates = (0*xstep, 27*ystep)
	if gridNum == 28:
		cellCoordinates = (0*xstep, 28*ystep)
	if gridNum == 29:
		cellCoordinates = (0*xstep, 29*ystep)
	if gridNum == 30:
		cellCoordinates = (0*xstep, 30*ystep)



"""








