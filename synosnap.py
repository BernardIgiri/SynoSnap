#!/usr/bin/env python
import os
import yaml
import sys

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
	return

main(sys.argv)
