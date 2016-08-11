class SnapshotUpdater:
	def __init__(self, sourceFolder, destinationFolder, startTime, fileHandler):
		this.sourceFolder = sourceFolder
		this.destinationFolder = destinationFolder
		this.startTime = startTime
		this.fh = fileHandler
		this.previousPeriod = null

	def process(period):
		if period.getNumOfSnapshots() == 0
			return

		periodFolder = this.getPeriodFolder(period)
		if !this.fh.ifFolderExists(periodFolder):
			this.fh.createFolder(periodFolder)
			lastUpdateTime = startTime
			if this.previousPeriod == null:
				this.copySource(periodFolder)
		else:
			lastUpdateTime = this.fh.getTimeStamp(periodFolder)
		if (startTime - lastUpdateTime) > period.getPeriodInSeconds():
			this.shiftFolders(periodFolder, period.getNumOfSnapshots())

			for i in range(period.getNumOfSnapshots()-2, -1, -1):
				entryFolder = fileHandler.joinPaths(periodFolder, str(i))
				if i < 1 and !fileHandler.ifFolderExists(entryFolder):
					file
		this.previousPeriod = period

	def shiftFolders(periodFolder, numOfSnapshots):
		this.fh.touchFolder(periodFolder)
		entryFolder = this.getEntryFolder(periodFolder, numOfSnapshots -1)
		this.fh.deleteFolder(entryFolder)
		for i in range(numOfSnapshots, 0, -1):
			entrySrc = this.getEntryFolder(periodFolder, i-1)
			entryDest = this.getEntryFolder(periodFolder, i)
			this.fh.moveFolder(entrySrc, entryDest)

	def getPeriodFolder(period):
		return this.fh.joinPaths(destinationFolder, period.getName())

	def getEntryFolder(periodFolder, entryNumber):
		return this.fh.joinPaths(periodFolder,str(entryNumber))

	def copySource(periodFolder):
		entryFolder = this.getEntryFolder(periodFolder, 0)
		this.fh.copyFolder(this.sourceFolder, entryFolder)
		this.fh.touchFolder(periodFolder)
