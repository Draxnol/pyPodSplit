from pydub import AudioSegment
from datetime import datetime
import os

def loadFile():
	print('enter name')
	filename = input()
	
	nums = []
	while True:
		print('enter number of end of a segment')
		num = input()
		if num == 'stop':
			break
		intnum = int(num)
		nums.append(intnum * 60000)
	beginSliceing(nums,filename)


def beginSliceing(listOfNumbers, filename):
	#load file
	print('loading file')
	audioSeg = AudioSegment.from_file(filename)
	print('Done Loading file.')
	print()
	
	#Split file
	startSlice = 0
	fileNum = 0
	print('beginning splitting')
	for i in listOfNumbers:
		fileVarName = "tale%i.mp3" % fileNum
		#increment file number.
		fileNum += 1
		#Set the slice start and slice uptill first number in list.
		toExport = audioSeg[startSlice:i]
		#set the new start slice to the previous slice number
		startSlice = i
		#export the file
		toExport.export(fileVarName, format='mp3')
		#print status
		print('done file')
	print('Task completed.')

loadFile()