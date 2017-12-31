from pydub import AudioSegment

class FileHandler():
    def __init__(self):
        self.filename = ''
        self.splitCount = 0
        self.prefix = 'test'
    def setFileName(self, filename):
        self.filename = filename
    def loadFile(self):
        self.file = AudioSegment.from_file(self.filename)
        print('file loaded')
    def splitFile(self,splitTimes):
        startSlice = 0
        for i in splitTimes:
            fileVarName = '{}{}.mp3'.format(self.prefix, self.splitCount)
            self.splitCount += 1
            toExport = self.file[startSlice:i]
            startSlice = i
            toExport.export(fileVarName, format='mp3')
            print(fileVarName + ' done')
