# Snap shot time periods
import datetime

class TimePeriod:
	def __init__(self):
		self.numOfSnapshots = 0
	def setNumOfSnapshots(self, numOfSnapshots):
		self.numOfSnapshots = numOfSnapshots
	def getNumOfSnapshots(self):
		return self.numOfSnapshots
	@staticmethod
	def getTimePeriods():
		return [
			Hourly(),
			Daily(),
			Weekly(),
			Monthly()
		]

class Hourly(TimePeriod):
	def getPeriodInSeconds(self):
		return 3600;
	def getName(self):
		return "hourly"

class Daily(TimePeriod):
	def getPeriodInSeconds(self):
		return 86400;
	def getName(self):
		return "daily"

class Weekly(TimePeriod):
	def getPeriodInSeconds(self):
		return 604800;
	def getName(self):
		return "weekly"

class Monthly(TimePeriod):
	def getPeriodInSeconds(self):
		return 2628000;
	def getName(self):
		return "monthly"
