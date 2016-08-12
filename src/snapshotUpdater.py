class SnapshotUpdater:
	def __init__(self, sourceFolder, destinationFolder, startTime, fileHandler):
		self.sourceFolder = sourceFolder
		self.destinationFolder = destinationFolder
		self.startTime = startTime
		self.fh = fileHandler
		self.previousPeriod = None

	def process(self, period):
		if period.getNumOfSnapshots() > 0:
			periodFolder = self.getPeriodFolder(period)
			if not self.fh.ifFolderExists(periodFolder):
				self.fh.createFolder(periodFolder)
				lastUpdateTime = self.startTime
				if self.previousPeriod == None:
					self.copySource(periodFolder)
			else:
				lastUpdateTime = self.fh.getTimeStamp(periodFolder)
			if (self.startTime - lastUpdateTime) > period.getPeriodInSeconds():
				self.shiftFolders(periodFolder, period.getNumOfSnapshots())
			self.previousPeriod = period

	def shiftFolders(self, periodFolder, numOfSnapshots):
		entryFolder = self.getEntryFolder(periodFolder, numOfSnapshots -1)
		if self.fh.ifFolderExists(entryFolder):
			self.fh.deleteFolder(entryFolder)
		for i in range(numOfSnapshots, 0, -1):
			entrySrc = self.getEntryFolder(periodFolder, i-1)
			entryDest = self.getEntryFolder(periodFolder, i)
			if self.fh.ifFolderExists(entrySrc):
				self.fh.moveFolder(entrySrc, entryDest)
		self.copySource(periodFolder)

	def getPeriodFolder(self, period):
		return self.fh.joinPaths(self.destinationFolder, period.getName())

	def getEntryFolder(self, periodFolder, entryNumber):
		return self.fh.joinPaths(periodFolder,str(entryNumber))

	def copySource(self, periodFolder):
		copySourceFolder = self.sourceFolder
		if self.previousPeriod != None:
			copySourcePeriodFolder = self.getPeriodFolder(self.previousPeriod)
			copySourceFolder = self.getEntryFolder(copySourcePeriodFolder, 0)
		self.fh.touchFolder(periodFolder, self.startTime)
		entryFolder = self.getEntryFolder(periodFolder, 0)
		self.fh.copyFolder(copySourceFolder, entryFolder)
