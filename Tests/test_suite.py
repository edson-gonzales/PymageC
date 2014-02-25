from coverage import coverage
cov = coverage()
cov.start()

import unittest

from file_manager_test import FileManagerTest
from image_handler_test import ImageManagerTest
from search_duplicate_by_name_test import SearchDuplicateByNameTest
from search_duplicate_by_size_test import SearchDuplicateBySizeTest
from search_duplicate_by_root_mean_square import SearchDuplicateByRootMeanSquareTest

suite = unittest.TestSuite()

suite.addTests(unittest.makeSuite(FileManagerTest))
suite.addTests(unittest.makeSuite(ImageManagerTest))
suite.addTests(unittest.makeSuite(SearchDuplicateByNameTest))
suite.addTests(unittest.makeSuite(SearchDuplicateBySizeTest))
suite.addTests(unittest.makeSuite(SearchDuplicateByRootMeanSquareTest))

unittest.TextTestRunner(verbosity = 2).run(suite)
cov.stop()
cov.html_report(directory='report')