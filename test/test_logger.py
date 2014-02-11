import unittest
import os
os.sys.path.append("../source")
from libs.logger import LoggerManager
from libs.constant import *

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.pymage_log = LoggerManager()

    def test_verify_that_a_info_message_is_logged_to_the_log_file(self):
        self.pymage_log.info(INFO_MESSAGE)
        log_content = self.pymage_log.get_log()
        self.assertTrue(INFO_MESSAGE in log_content)

    def test_verify_that_a_error_message_is_logged_to_the_log_file(self):
        self.pymage_log.error(ERROR_MESSAGE)
        log_content = self.pymage_log.get_log()
        self.assertTrue(ERROR_MESSAGE in log_content)

    def test_verify_that_a_debug_message_is_logged_to_the_log_file(self):
        self.pymage_log.debug(DEBUG_MESSAGE)
        log_content = self.pymage_log.get_log()
        self.assertTrue(DEBUG_MESSAGE in log_content)

    def test_verify_that_a_warning_message_is_logged_to_the_log_file(self):
        self.pymage_log.warning(WARNING_MESSAGE)
        log_content = self.pymage_log.get_log()
        self.assertTrue(WARNING_MESSAGE in log_content)

    def test_verify_that_a_critical_message_is_logged_to_the_log_file(self):
        self.pymage_log.critical(CRITICAL_MESSAGE)
        log_content = self.pymage_log.get_log()
        self.assertTrue(CRITICAL_MESSAGE in log_content)

    def test_verify_that_the_log_file_can_be_cleaned(self):
        self.pymage_log.clear_log()
        log_content = self.pymage_log.get_log()
        self.assertTrue(not log_content)

    def tearDown(self):
        self.pymage_log.clear_log()

if __name__ == '__main__':
    unittest.main()
