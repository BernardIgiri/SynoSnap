# SynoSnap

## Overview

SynoSnap is a backup snapshot maintaining script designed to have minimal enough requirements that it can run on a Synology NAS without the pain of installing ipkg. Hardlink copying is used to minimize disk space foot print.

## Requirements
 - Python 2.7+
 - [PyYAML](http://pyyaml.org/) used for YAML parsing.
 - Linux

## Installation
 - Download and install PyYAML from [pyyaml.org](http://pyyaml.org/)
 - Download and extract this project

## Usage
Each run updates all snapshots based on current time.
You should run this script via Chron with a frequency matching the shortest
time period that you are keeping snapshots for.

**Execute with:**
```bash
./synosnap.py configfile options
```
**Options:**

--dry-run
: Dry run (no files will be written to disk)

## Configuration
Create a yaml configuration file with the following parameters
```yaml
hourly: 0 # number of hourly snapshots to keep
daily: 0 # number of daily snapshots to keep
weekly: 0 # number of weekly snapshots to keep
monthly: 0 # number of monthly snapshots to keep
source: "" # path to folder generate snapshots of *required
destination: "" # path to folder to store snapshots *required
```
