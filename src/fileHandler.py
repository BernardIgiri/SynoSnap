# Disk operations
import os, shutil

class FileHandlerBase:
	def joinPaths(pathLeft, pathRight):
		return os.path.join(pathLeft, pathRight)
	def ifFolderExists(folder):
		return os.path.exists(folder)
	def getTimeStamp(folder):
		return os.stat(folder).st_mtime

class DryRunFileHandler(FileHandlerBase):
	def createFolder(folder):
		print "Create " + folder
	def deleteFolder(folder):
		print "Delete " + folder
	def moveFolder(source, destination):
		print "Move " + source + " to " + destination;
	def copyFolder(source, destination):
		print "Copy " + source + " to " + destination;
	def touchFolder(folder, time):
		return

class LiveFileHandler(FileHandlerBase):
	def __init__(self):
		self.logger = DryRunFileHandler()
	def createFolder(folder):
		self.logger.createFolder(folder)
		os.makedirs(folder)
	def deleteFolder(folder):
		self.logger.deleteFolder(folder)
		shutil.rmtree(folder)
	def moveFolder(source, destination):
		self.logger.moveFolder(source, destination)
		shutil.move(source, destination)
	def copyFolder(source, destination):
		self.logger.copyFolder(source, destination)
		os.system('cp -al "' + source + '" "' + destination + '"')
	def touchFolder(folder, time):
		os.system('touch "' + folder + '" -t "' + time + '"')
