import sys, os
sys.path.insert(0, os.path.abspath('../src'))
import unittest, mock, fileHandler

class TestFileHandlerBase(unittest.TestCase):

	def setUp(self):
		self.fh = fileHandler.FileHandlerBase()

	@mock.patch('fileHandler.os.path')
	def test_joinPaths(self, mock_obj):
		expected = "joined"
		mock_obj.join.return_value = expected
		actual = self.fh.joinPaths('left','right')
		mock_obj.join.assert_called_with('left','right')
		self.assertEqual(expected, actual)

	@mock.patch('fileHandler.os.path')
	def test_ifFolderExists(self, mock_obj):
		expected = True
		mock_obj.exists.return_value = expected
		actual = self.fh.ifFolderExists('some Path')
		mock_obj.exists.assert_called_with('some Path')
		self.assertEqual(expected, actual)

	@mock.patch('fileHandler.os')
	def test_getTimeStamp(self, mock_obj):
		expected = 100
		obj = lambda: None
		obj.st_mtime = expected
		mock_obj.stat.return_value = obj
		actual = self.fh.getTimeStamp('some Path')
		mock_obj.stat.assert_called_with('some Path')
		self.assertEqual(expected, actual)

class TestLiveFileHandler(unittest.TestCase):

	def setUp(self):
		self.fh = fileHandler.LiveFileHandler()

	@mock.patch.object(fileHandler.DryRunFileHandler, 'createFolder')
	@mock.patch('fileHandler.os')
	def test_createFolder(self, mock_obj, mock_logger):
		self.fh.createFolder('some Path')
		mock_obj.makedirs.assert_called_with('some Path')
		mock_logger.assert_called_with('some Path')

	@mock.patch.object(fileHandler.DryRunFileHandler, 'deleteFolder')
	@mock.patch('fileHandler.shutil')
	def test_deleteFolder(self, mock_obj, mock_logger):
		self.fh.deleteFolder('some Path')
		mock_obj.rmtree.assert_called_with('some Path')
		mock_logger.assert_called_with('some Path')

	@mock.patch.object(fileHandler.DryRunFileHandler, 'moveFolder')
	@mock.patch('fileHandler.shutil')
	def test_moveFolder(self, mock_obj, mock_logger):
		self.fh.moveFolder('some Path','some Other Path')
		mock_obj.move.assert_called_with('some Path','some Other Path')
		mock_logger.assert_called_with('some Path','some Other Path')

	@mock.patch.object(fileHandler.DryRunFileHandler, 'copyFolder')
	@mock.patch('fileHandler.os')
	def test_copyFolder(self, mock_obj, mock_logger):
		self.fh.copyFolder('some Path','some Other Path')
		mock_obj.system.assert_called_with('cp -al "some Path" "some Other Path"')
		mock_logger.assert_called_with('some Path','some Other Path')

	@mock.patch('fileHandler.os')
	def test_touchFolder(self, mock_obj):
		self.fh.touchFolder('some Path', 1471132800)
		mock_obj.system.assert_called_with('touch "some Path" -d "2016-08-13 20:00:00"')

if __name__ == '__main__':
    unittest.main()
