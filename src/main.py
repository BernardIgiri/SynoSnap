import yaml, timePeriod, fileHandler, snapshotUpdater, time

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
	if isDryRun:
		fileHandler = fileHandler.DryRunFileHandler()
	else:
		fileHandler = fileHandler.LiveFileHandler()
	timePeriods = timePeriod.TimePeriod.getTimePeriods()
	for period in timePeriods:
		if configuration.has_key(period.getName()):
			period.setNumOfSnapshots = configuration[period.getName]
	if !configuration.has_key('output'):
		print "Invalid configuration in " + configFile + ". See README.md"
		return
	updater = snapshotUpdater.SnapshotUpdater(
		configuration['source'],
		configuration['destination'],
		time.gmTime(),
		fileHandler
	)
	for period in timePeriods:
		updater.process(period)
	return
