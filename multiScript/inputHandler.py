class inputHandler():
	def __init__(self):
		self.filename = ''
	def getFileName(self):
		name = input('get file name')
		return name
	def getSplitTimes(self):
		sTimes = []
		while True:
			print("Please Enter a slice time")
			num = input()
			if num == 'stop':
				break
			intnum = int(num)
			sTimes.append(intnum * 60000)
		return sTimes