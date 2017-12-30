import fileReader
import inputHandler
import fileHandler
import os

inputStuff = inputHandler.inputHandler()
fileStuff = fileHandler.FileHandler()
def getMode():
	mode = inputStuff.determineAutoOrManual()
	if mode == 'man':
		getFileInfo()
		loadAudioFile()
	elif mode =='auto':
		fileProcesser = fileReader.FileReader()
		fileProcesser.processFile(inputStuff.getFileName())
def getFileInfo():
	filename = inputStuff.getFileName()
	if os.path.isfile(filename):
		fileStuff.setFileName(filename)
	else:
		print('file not found, please try again.')
		getFileInfo()
def loadAudioFile():
	try:
		fileStuff.loadFile()
	except Exception:
		print('error: not an audio file')
		getFileInfo()
	fileStuff.splitFile(inputStuff.getSplitTimes())
getMode()
