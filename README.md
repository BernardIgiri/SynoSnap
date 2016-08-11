# SynoSnap

## Overview

SynoSnap is a backup snapshot maintaining script designed to have minimal enough requirements that it can run on a Synology NAS without the pain of installing ipkg.

## Requirements
 - Python 2.7+
 - [PyYAML](http://pyyaml.org/) used for YAML parsing.

## Usage
Each run updates all snapshots based on current time.

**Execute with:**
```bash
./synosnap.py configfile options
```
**Options:**

-r
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
