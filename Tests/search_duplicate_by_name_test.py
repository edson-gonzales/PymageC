import unittest
import sys
sys.path.append("../source/libs")
from FileManager import FileManager
from SearchDuplicateByName import SearchDuplicateByName
import os

class SearchDuplicateByNameTest(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager()
        self.search_by_name = SearchDuplicateByName()
        self.current_path = os.getcwd()

    def test_search_duplicate_by_name_returns_images_duplicated_in_a_directory_and_within_subfolders(self):
        folder = "/input"
        path_directory = self.current_path + folder
        list_images = self.file_manager.list_image_from_path(path_directory)
        self.assertEquals(['pregoneroOficial.jpg', 'apple.bmp'], self.search_by_name.search_duplicate(list_images))

    def test_search_duplicate_by_name_returns_a_empty_list_when_none_image_duplicated(self):
        folder = "/input/moreimages"
        path_directory = self.current_path + folder
        list_images = self.file_manager.list_image_from_path(path_directory)
        self.assertEquals([], self.search_by_name.search_duplicate(list_images))
    
    def test_extract_entire_path_of_each_image_duplicated_returns_path_directory_for_each_image(self):
        folder = "/input"
        path_directory = self.current_path + folder
        list_images = self.file_manager.list_image_from_path(path_directory)
        list_images_duplicated = self.search_by_name.search_duplicate(list_images)
        self.assertEquals(4,len(self.search_by_name.extract_entire_path_of_each_image_duplicated(list_images_duplicated, path_directory)))    

    def test_extract_entire_path_of_each_image_duplicated_returns_empty_list_when_none_image_duplicate(self):
        folder = "/input/moreimages"
        path_directory = self.current_path + folder
        list_images = self.file_manager.list_image_from_path(path_directory)
        list_images_duplicated = self.search_by_name.search_duplicate(list_images)
        self.assertEquals(0,len(self.search_by_name.extract_entire_path_of_each_image_duplicated(list_images_duplicated, path_directory)))

