import unittest
from PIL import Image
import sys
sys.path.append("../source/libs")
from FileManager import FileManager
from SearchDuplicateRootMeanSquare import SearchDuplicateRootMeanSquare
import os

class SearchDuplicateByRootMeanSquareTest(unittest.TestCase):
    def setUp(self):
        self.file_manager = FileManager()
        self.search_by_root_mean_square = SearchDuplicateRootMeanSquare()
        self.current_path = os.getcwd()

    def test_root_maean_square_returns_the_result_of_compare_two_images(self):
        image1 = "/input/apple.bmp"
        path_image1 = self.current_path + image1
        image2 = "/input/pregoneroOficial.jpg"
        path_image2 = self.current_path + image2
        image_open1 = Image.open(path_image1)
        image_open2 = Image.open(path_image2)
        self.assertEquals(151.29026130199338, self.search_by_root_mean_square.root_maean_square(image_open1, image_open2))

    def test_compare_all_images_returns_list_with_images_duplicated_using_root_mean_square_alghoritm(self):
        path = self.current_path + "/input"
        list_images_paths = self.file_manager.list_image_names_with_path_directory(path)
        self.assertEquals(4, len(self.search_by_root_mean_square.compare_all_images(list_images_paths, path)))

