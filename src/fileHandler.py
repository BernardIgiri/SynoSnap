# Disk operations
import os, shutil, datetime

class FileHandlerBase:
	def joinPaths(self, pathLeft, pathRight):
		return os.path.join(pathLeft, pathRight)
	def ifFolderExists(self, folder):
		return os.path.exists(folder)
	def getTimeStamp(self, folder):
		return os.stat(folder).st_mtime

class DryRunFileHandler(FileHandlerBase):
	def createFolder(self, folder):
		print "Create " + folder
	def deleteFolder(self, folder):
		print "Delete " + folder
	def moveFolder(self, source, destination):
		print "Move " + source + " to " + destination;
	def copyFolder(self, source, destination):
		print "Copy " + source + " to " + destination;
	def touchFolder(self, folder, time):
		return

class LiveFileHandler(FileHandlerBase):
	def __init__(self):
		self.logger = DryRunFileHandler()
	def createFolder(self, folder):
		self.logger.createFolder(folder)
		os.makedirs(folder)
	def deleteFolder(self, folder):
		self.logger.deleteFolder(folder)
		shutil.rmtree(folder)
	def moveFolder(self, source, destination):
		self.logger.moveFolder(source, destination)
		shutil.move(source, destination)
	def copyFolder(self, source, destination):
		self.logger.copyFolder(source, destination)
		os.system('cp -al "' + source + '" "' + destination + '"')
	def touchFolder(self, folder, time):
		dateString = datetime.datetime.fromtimestamp(
		        time
		    ).strftime('%Y-%m-%d %H:%M:%S')
		os.system('touch "' + folder + '" -d "' + dateString + '"')
