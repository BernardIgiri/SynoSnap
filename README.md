# SynoSnap
Backup snapshoting script for use on Synology NAS.

## Dependancies

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
output: "" # path to output folder to store snapshots *required
```
