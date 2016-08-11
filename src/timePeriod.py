# Snap shot time periods
import datetime

class TimePeriod:
	def __init__(self):
		this.numOfSnapshots = 0
	def setNumOfSnapshots(numOfSnapshots):
		this.numOfSnapshots = numOfSnapshots
	def getNumOfSnapshots():
		return this.numOfSnapshots
	@staticmethod
	def getTimePeriods():
		return [
			Hourly(),
			Daily(),
			Weekly(),
			Monthly()
		]

class Hourly(TimePeriod):
	def getPeriodInSeconds():
		return 3600;
	def getName():
		return "hourly"

class Daily(TimePeriod):
	def getPeriodInSeconds():
		return 86400;
	def getName():
		return "daily"

class Weekly(TimePeriod):
	def getPeriodInSeconds():
		return 604800;
	def getName():
		return "weekly"

class Monthly(TimePeriod):
	def getPeriodInSeconds():
		return 2628000;
	def getName():
		return "monthly"
