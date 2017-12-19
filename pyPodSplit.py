from pydub import AudioSegment

def getFileName():
	filename = input('Please enter the file name')
	return filename
def loadFile():
	fileToLoad = getFileName()
	file = AudioSegment.from_file(fileToLoad)
	return file
def getSliceTimes():
	sTimes = []
	while True:
		print("Please Enter a slice time")
		num = input()
		if num == 'stop':
			break
		intnum = int(num)
		sTimes.append(intnum * 60000)
	return sTimes
def startSlicing():
	startSlice = 0
	fileNum = 0
	file = loadFile()
	slicetimes = getSliceTimes()
	for i in slicetimes:
		fileVarName = 'tale%i.mp3' %fileNum
		fileNum += 1
		toExport = file[startSlice:i]
		startSlice = i
		toExport.export(fileVarName, format='mp3')
		print('done file')
	print('task completed')
startSlicing()