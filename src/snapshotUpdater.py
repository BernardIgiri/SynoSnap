class SnapshotUpdater:
	def __init__(self, sourceFolder, destinationFolder, startTime, fileHandler):
		this.sourceFolder = sourceFolder
		this.destinationFolder = destinationFolder
		this.startTime = startTime
		this.fh = fileHandler
		this.previousPeriod = null

	def process(period):
		if period.getNumOfSnapshots() > 0:
			periodFolder = this.getPeriodFolder(period)
			if !this.fh.ifFolderExists(periodFolder):
				this.fh.createFolder(periodFolder)
				lastUpdateTime = this.startTime
				if this.previousPeriod == null:
					this.copySource(periodFolder)
			else:
				lastUpdateTime = this.fh.getTimeStamp(periodFolder)
			if (this.startTime - lastUpdateTime) > period.getPeriodInSeconds():
				this.shiftFolders(periodFolder, period.getNumOfSnapshots())
			this.previousPeriod = period

	def shiftFolders(periodFolder, numOfSnapshots):
		entryFolder = this.getEntryFolder(periodFolder, numOfSnapshots -1)
		this.fh.deleteFolder(entryFolder)
		for i in range(numOfSnapshots, 0, -1):
			entrySrc = this.getEntryFolder(periodFolder, i-1)
			entryDest = this.getEntryFolder(periodFolder, i)
			this.fh.moveFolder(entrySrc, entryDest)
		this.copySource(periodFolder)

	def getPeriodFolder(period):
		return this.fh.joinPaths(this.destinationFolder, period.getName())

	def getEntryFolder(periodFolder, entryNumber):
		return this.fh.joinPaths(periodFolder,str(entryNumber))

	def copySource(periodFolder):
		copySourceFolder = this.sourceFolder
		if this.previousPeriod != null:
			copySourceFolder =
				this.getEntryFolder(
					this.getPeriodFolder(this.previousPeriod),
					0
				)
		this.fh.touchFolder(periodFolder, this.startTime)
		entryFolder = this.getEntryFolder(periodFolder, 0)
		this.fh.copyFolder(copySourceFolder, entryFolder)
