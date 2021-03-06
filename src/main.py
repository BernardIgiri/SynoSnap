import timePeriod, fileHandler, snapshotUpdater, time, re

def main(arguments):
	if len(arguments) < 2:
		print "Not enough arguments. See README.md"
		return
	configFile = arguments[1];
	isDryRun   = False
	for i in range(2, len(arguments)):
		if arguments[i] == "--dry-run":
			print "Dry run only, no files will be altered."
			isDryRun = True
	configuration = {}
	pattern = re.compile("\s+")
	with open(configFile, 'r') as stream:
		for line in stream:
			entry = pattern.split(line)
			configuration[entry[0]] = entry[1]
	if isDryRun:
		fh = fileHandler.DryRunFileHandler()
	else:
		fh = fileHandler.LiveFileHandler()
	timePeriods = timePeriod.TimePeriod.getTimePeriods()
	for period in timePeriods:
		if configuration.has_key(period.getName()):
			period.setNumOfSnapshots(int(configuration[period.getName()]))
	if not configuration.has_key('destination') or not configuration.has_key('source'):
		print "Invalid configuration in " + configFile + ". See README.md"
		return
	updater = snapshotUpdater.SnapshotUpdater(
		configuration['source'],
		configuration['destination'],
		int(time.time()),
		fh
	)
	for period in timePeriods:
		updater.process(period)
	print "Finished."
	return
