class inputHandler():
	def __init__(self):
		self.filename = ''
	def getFileName(self):
		name = input('please enter file name: \n')
		return name
	def getSplitTimes(self):
		sTimes = []
		while True:
			print("Please Enter a slice time, the first slice starts at 0")
			num = input()
			if num == 'stop':
				break
			else:
				try:
					intnum = int(num)
					sTimes.append(intnum * 60000)
				except ValueError:
					print('Error not a number')
					continue
		return sTimes