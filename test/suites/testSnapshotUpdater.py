import sys, os
sys.path.insert(0, os.path.abspath('../src'))
import unittest, mock, snapshotUpdater, fileHandler, timePeriod

class TestSnapshotUpdater(unittest.TestCase):

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'shiftFolders')
	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'getTimeStamp')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'createFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_process_unitialized_lessThanPeriodElapsed(self,
		mock_ifFolderExists,
		mock_createFolder,
		mock_getTimeStamp,
		mock_copySource,
		mock_shiftFolders):
		period = timePeriod.Hourly()
		period.setNumOfSnapshots(2)
		mock_ifFolderExists.return_value = False
		mock_getTimeStamp.return_value = 0
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 3599
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.process(period)
		assert not mock_shiftFolders.called
		assert mock_copySource.called
		assert mock_createFolder.called
		mock_createFolder.assert_called_with('snapshots/hourly')
		mock_copySource.assert_called_with('snapshots/hourly')

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'shiftFolders')
	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'getTimeStamp')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'createFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_process_unitialized_moreThanPeriodElapsed(self,
		mock_ifFolderExists,
		mock_createFolder,
		mock_getTimeStamp,
		mock_copySource,
		mock_shiftFolders):
		period = timePeriod.Hourly()
		period.setNumOfSnapshots(2)
		mock_ifFolderExists.return_value = False
		mock_getTimeStamp.return_value = 0
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 3600
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.process(period)
		assert not mock_shiftFolders.called
		assert mock_copySource.called
		assert mock_createFolder.called
		mock_createFolder.assert_called_with('snapshots/hourly')
		mock_copySource.assert_called_with('snapshots/hourly')

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'shiftFolders')
	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'getTimeStamp')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'createFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_process_followUpSnapshot_lessThanPeriodElapsed(self,
		mock_ifFolderExists,
		mock_createFolder,
		mock_getTimeStamp,
		mock_copySource,
		mock_shiftFolders):
		period = timePeriod.Hourly()
		period.setNumOfSnapshots(2)
		mock_ifFolderExists.return_value = True
		mock_getTimeStamp.return_value = 0
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 3599
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.process(period)
		assert not mock_shiftFolders.called
		assert not mock_copySource.called
		assert not mock_createFolder.called

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'shiftFolders')
	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'getTimeStamp')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'createFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_process_followUpSnapshot_moreThanPeriodElapsed(self,
		mock_ifFolderExists,
		mock_createFolder,
		mock_getTimeStamp,
		mock_copySource,
		mock_shiftFolders):
		period = timePeriod.Hourly()
		period.setNumOfSnapshots(2)
		mock_ifFolderExists.return_value = True
		mock_getTimeStamp.return_value = 0
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 3600
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.process(period)
		assert mock_shiftFolders.called
		assert not mock_copySource.called
		assert not mock_createFolder.called
		mock_shiftFolders.assert_called_with('snapshots/hourly', 2)

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'shiftFolders')
	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'getTimeStamp')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'createFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_process_unitializedTwoPeriods_lessThanPeriodElapsed(self,
		mock_ifFolderExists,
		mock_createFolder,
		mock_getTimeStamp,
		mock_copySource,
		mock_shiftFolders):
		period1 = timePeriod.Hourly()
		period1.setNumOfSnapshots(2)
		period2 = timePeriod.Daily()
		period2.setNumOfSnapshots(2)
		mock_ifFolderExists.return_value = False
		mock_getTimeStamp.return_value = 0
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 3599
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.process(period1)
		assert not mock_shiftFolders.called
		assert mock_copySource.called
		assert mock_createFolder.called
		mock_createFolder.assert_called_with('snapshots/hourly')
		mock_copySource.assert_called_with('snapshots/hourly')
		mock_createFolder.reset_mock()
		mock_copySource.reset_mock()
		updater.process(period2)
		assert not mock_shiftFolders.called
		assert not mock_copySource.called
		assert mock_createFolder.called
		mock_createFolder.assert_called_with('snapshots/daily')

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'shiftFolders')
	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'getTimeStamp')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'createFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_process_nextIncrement_lessThanPeriodElapsed(self,
		mock_ifFolderExists,
		mock_createFolder,
		mock_getTimeStamp,
		mock_copySource,
		mock_shiftFolders):
		period1 = timePeriod.Hourly()
		period1.setNumOfSnapshots(2)
		period2 = timePeriod.Daily()
		period2.setNumOfSnapshots(2)
		mock_ifFolderExists.return_value = True
		mock_getTimeStamp.return_value = 0
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 3600
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.process(period1)
		assert mock_shiftFolders.called
		assert not mock_copySource.called
		assert not mock_createFolder.called
		mock_shiftFolders.assert_called_with('snapshots/hourly', 2)
		mock_shiftFolders.reset_mock()
		updater.process(period2)
		assert not mock_shiftFolders.called
		assert not mock_copySource.called
		assert not mock_createFolder.called

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'shiftFolders')
	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'getTimeStamp')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'createFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_process_nextIncrement_moreThanPeriodElapsed(self,
		mock_ifFolderExists,
		mock_createFolder,
		mock_getTimeStamp,
		mock_copySource,
		mock_shiftFolders):
		period1 = timePeriod.Hourly()
		period1.setNumOfSnapshots(2)
		period2 = timePeriod.Daily()
		period2.setNumOfSnapshots(2)
		mock_ifFolderExists.return_value = True
		mock_getTimeStamp.return_value = 0
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 86400
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.process(period1)
		assert mock_shiftFolders.called
		assert not mock_copySource.called
		assert not mock_createFolder.called
		mock_shiftFolders.assert_called_with('snapshots/hourly', 2)
		mock_shiftFolders.reset_mock()
		updater.process(period2)
		assert mock_shiftFolders.called
		assert not mock_copySource.called
		assert not mock_createFolder.called
		mock_shiftFolders.assert_called_with('snapshots/daily', 2)

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'deleteFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'moveFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_shiftFolders_noFolders(self,
		mock_ifFolderExists,
		mock_moveFolder,
		mock_deleteFolder,
		mock_copySource):
		mock_ifFolderExists.return_value = False
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 0
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.shiftFolders("snapshots/hourly", 3)
		assert not mock_moveFolder.called
		assert not mock_deleteFolder.called
		assert mock_copySource.called
		mock_copySource.assert_called_with('snapshots/hourly')

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'deleteFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'moveFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_shiftFolders_lessThanMaxFolders(self,
		mock_ifFolderExists,
		mock_moveFolder,
		mock_deleteFolder,
		mock_copySource):
		mock_ifFolderExists.side_effect = [False, False, True]
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 0
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.shiftFolders("snapshots/hourly", 3)
		assert mock_moveFolder.called
		assert not mock_deleteFolder.called
		assert mock_copySource.called
		mock_moveFolder.assert_called_with('snapshots/hourly/0', 'snapshots/hourly/1')
		mock_copySource.assert_called_with('snapshots/hourly')

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'deleteFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'moveFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_shiftFolders_halfwayFolders(self,
		mock_ifFolderExists,
		mock_moveFolder,
		mock_deleteFolder,
		mock_copySource):
		mock_ifFolderExists.side_effect = [False, True, True]
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 0
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.shiftFolders("snapshots/hourly", 3)
		assert mock_moveFolder.called
		assert not mock_deleteFolder.called
		assert mock_copySource.called
		mock_moveFolder.assert_has_calls([
				mock.call('snapshots/hourly/1', 'snapshots/hourly/2'),
				mock.call('snapshots/hourly/0', 'snapshots/hourly/1')
			])
		mock_copySource.assert_called_with('snapshots/hourly')

	@mock.patch.object(snapshotUpdater.SnapshotUpdater, 'copySource')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'deleteFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'moveFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'ifFolderExists')
	def test_shiftFolders_atMaxFolders(self,
		mock_ifFolderExists,
		mock_moveFolder,
		mock_deleteFolder,
		mock_copySource):
		mock_ifFolderExists.return_value = True
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 0
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.shiftFolders("snapshots/hourly", 3)
		assert mock_moveFolder.called
		assert mock_deleteFolder.called
		assert mock_copySource.called
		mock_deleteFolder.assert_called_with('snapshots/hourly/2')
		mock_copySource.assert_called_with('snapshots/hourly')
		mock_moveFolder.assert_has_calls([
				mock.call('snapshots/hourly/1', 'snapshots/hourly/2'),
				mock.call('snapshots/hourly/0', 'snapshots/hourly/1')
			])

	@mock.patch.object(fileHandler.DryRunFileHandler, 'touchFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'copyFolder')
	def test_copySource_noPreviousPeriod(self,
		mock_copyFolder,
		mock_touchFolder):
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 12345
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.copySource('snapshots/monthly')
		mock_touchFolder.assert_called_with('snapshots/monthly', 12345)
		mock_copyFolder.assert_called_with('source', 'snapshots/monthly/0')

	@mock.patch.object(fileHandler.DryRunFileHandler, 'touchFolder')
	@mock.patch.object(fileHandler.DryRunFileHandler, 'copyFolder')
	def test_copySource_withPreviousPeriod(self,
		mock_copyFolder,
		mock_touchFolder):
		sourceFolder = "source"
		destinationFolder = "snapshots"
		startTime = 12345
		fh = fileHandler.DryRunFileHandler()
		updater = snapshotUpdater.SnapshotUpdater(sourceFolder, destinationFolder, startTime, fh)
		updater.previousPeriod = timePeriod.Hourly()
		updater.copySource('snapshots/monthly')
		mock_touchFolder.assert_called_with('snapshots/monthly', 12345)
		mock_copyFolder.assert_called_with('snapshots/hourly/0', 'snapshots/monthly/0')

if __name__ == '__main__':
    unittest.main()
