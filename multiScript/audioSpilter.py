import inputHandler
import fileHandler
import os

inputStuff = inputHandler.inputHandler()
fileStuff = fileHandler.FileHandler()

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

getFileInfo()
loadAudioFile()
