# SynoSnap

## Overview

SynoSnap is a backup snapshot maintaining script designed to have minimal enough requirements that it can run on a Synology NAS without the pain of installing ipkg. Hardlink copying is used to minimize disk space foot print.

## Requirements
 - Python 2.7+
 - Linux

## Installation
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
Create a text configuration file in the following format parameters
```
hourly      number_of_hourly_snapshots_to_keep
daily       number_of_hourly_snapshots_to_keep
weekly      number_of_hourly_snapshots_to_keep
monthly     number_of_hourly_snapshots_to_keep
source      path_to_folder_to_generate_snapshots_of
destination path_to_folder_to_store_snapshots
```
At the minimum you should specify source, destination, and at least 1 interval.

Here are a few examples
```
hourly      3
daily       7
weekly      4
monthly     6
source      /home
destination /snapshots
```

Minimal Example
```
weekly 3
source /home/
destination /snapshots/
```
