import os
import logging
from libs.singleton_metaclass import Singleton


class LoggerManager(object):

    __metaclass__ = Singleton

    def __init__(self, log_file_name="pymage.log"):
        """
        Default constructor method

        Parameter::
        log_file_name: Name of the log file
        """
        file_handler = self.get_file_handler(log_file_name)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_file_handler(self, log_file_name):
        """
        The method will convert the log_file_name in a absolute path to store the log file into
        log folder

        Parameter::
        log_file_name: Name of the log file
        """
        self.log_file_abs_path = os.path.abspath("../log/" + log_file_name)
        filehandler = logging.FileHandler(self.log_file_abs_path, 'a')
        return filehandler

    def debug(self, message):
        """
        This method write an debug message to the log file

        Parameter::
        message: Message to save on the log file

        """
        self.logger.debug(message)

    def warning(self, message):
        """
        This method write a warning message to the log file

        Parameter::
        message: Message to save on the log file

        """
        self.logger.warning(message)

    def critical(self, message):
        """
        This method write an critical message to the log file

        Parameter::
        message: Message to save on the log file

        """
        self.logger.critical(message)

    def error(self, message):
        """
        This method write an error message to the log file

        Parameter::
        message: Message to save on the log file

        """
        self.logger.error(message)

    def info(self, message):
        """
        This method write an info message to the log file

        Parameter::
        message: Message to save on the log file
        """
        self.logger.info(message)

    def get_log(self):
        """
        Return the content of the log
        """
        open_file = open(self.log_file_abs_path, 'r')
        read_log = open_file.read()
        open_file.close()
        return str(read_log)

    def clear_log(self):
        """
        Clear the content of the log
        """
        open_file = open(self.log_file_abs_path, 'w')
        open_file.truncate()
        open_file.close()