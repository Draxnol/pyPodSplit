import inputHandler
import fileHandler

inputStuff = inputHandler.inputHandler()
fileStuff = fileHandler.FileHandler()

filename = inputStuff.getFileName()
fileStuff.setFileName(filename)
fileStuff.loadFile()
fileStuff.splitFile(inputStuff.getSplitTimes())