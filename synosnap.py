#!/usr/bin/env python
import os, yaml, sys, shutil, datetime

def main(arguments):
	if len(arguments) < 2:
		print "Not enough arguments. See README.md"
		return
	configFile = arguments[1];
	isDryRun   = False
	for i in range(2, len(arguments)):
		if arguments[i] == "-r":
			isDryRun = True
	stream = file(configFile, 'r')
	configuration = yaml.load(stream)
	return

def updateSnapShot(timePeriod, nSnapshots, isDryRun):
	if isDryRun:
		fileHandler = DryRunFileHandler()
	else:
		fileHandler = LiveFileHandler()
	return

class FileHandlerBase:
	def ifFolderExists(folder):
		return os.path.exists(folder)
	def getTimeStamp(folder):
		return os.stat(folder).st_mtime

class DryRunFileHandler(FileHandlerBase):
	def deleteFolder(folder):
		print "Delete " + folder
	def moveFolder(folderA, folderB):
		print "Move " + folderA + " to " + folderB;
	def copyFolder(folderA, folderB):
		print "Copy " + folderA + " to " + folderB;
	def touchFolder(folder):
		return

class LiveFileHandler(FileHandlerBase):
	def _init_(self):
		self.logger = DryRunFileHandler()
	def deleteFolder(folder):
		self.logger.deleteFolder(folder)
		shutil.rmtree(folder)
	def moveFolder(folderA, folderB):
		self.logger.moveFolder(folderA, folderB)
		shutil.move(folderA, folderB)
	def copyFolder(folderA, folderB):
		self.logger.copyFolder(folderA, folderB)
		os.system('cp -al "' + folderA + '" "' + folderB + '"')
	def touchFolder(folder):
		os.system('touch "' + folder + "'")

main(sys.argv)
