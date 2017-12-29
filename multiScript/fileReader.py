from pydub import AudioSegment
import csv
class FileReader():
    def processFile(self,filename):
        with open(filename, newline='') as ofile:
            reader = csv.reader(ofile)
            for row in reader:
                storyTimes=[]
                storyNames = []
                fileName = ''
                for index,data in enumerate(row):
                    if index == 0:
                        print('title is: ' + data)
                        fileName = data
                    elif index > 0:
                        if index%2 == 0:
                            print('timestamp is: ' + data)
                            #append timestamp to array
                            intNum = int(data)
                            storyTimes.append(intNum * 60000)
                        else:
                            #append storyNames
                            print('story name is: ' + data)
                            storyNames.append(data)
                status = self.processAudio(fileName,storyTimes,storyNames)
                print('--------------')
                print(status)
                print('--------------')
            #This is where the for loop ends
            #This is where i operate on a file
            #filename, times and tale names
    def processAudio(self, fileName, storyTimes, storyNames):
        #load file
        startSlice = 0
        file = AudioSegment.from_file(fileName)
        for index, name in enumerate(storyNames):
            print('------'+str(index) + ' ' + name)
            fileSplitName = '{}.mp3'.format(name)
            toExport = file[startSlice:int(storyTimes[index])]
            startSlice = storyTimes[index]
            toExport.export(fileSplitName, format='mp3')
        return 'done'