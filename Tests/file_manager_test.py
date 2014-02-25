
import unittest
import sys
sys.path.append("../source/libs")
from FileManager import FileManager
import os

class FileManagerTest(unittest.TestCase):
       
    def setUp(self):
        
        self.file_manager= FileManager()
        self.path = os.getcwd()
        self.current_path = os.getcwd() + "/input"
        
    def test_get_current_path_return_the_current_path(self):
    
        self.assertEquals(self.path, self.file_manager.get_current_path())

    def test_list_image_from_path_return_a_list_with_images(self):
        
        self.assertEquals(['apple.bmp', 'pregoneroOficial.jpg', 'tank.png', 'apple.bmp', 'bmp.bmp', 'linux.png', 'pregoneroOficial.jpg', 'programmer.jpg', 'test.jpg'], self.file_manager.list_image_from_path(self.current_path))

    def test_list_image_from_path_return_a_list_with_images_with_three_matching_files_and_one_different(self):
        
        folder = "/moreimages"
        path = self.current_path + folder
        self.assertEquals(['apple.bmp', 'bmp.bmp', 'linux.png', 'pregoneroOficial.jpg', 'programmer.jpg', 'test.jpg'], self.file_manager.list_image_from_path(path))
    
    def test_list_image_from_path_return_a_empty_list_when_no_images_exist(self):
        
        folder="/empty"
        path = self.current_path + folder
        self.assertEquals([], self.file_manager.list_image_from_path(path))    

    def test_list_image_names_with_path_directory_returns_a_list_with_images_and_paths(self):
        
        self.assertEquals(9, len(self.file_manager.list_image_names_with_path_directory(self.current_path)))

    def test_list_image_names_with_path_directory_return_a_list_with_images_and_paths_with_three_matching_files_and_one_different(self):
        
        folder = "/moreimages"
        path = self.current_path + folder
        self.assertEquals(6, len(self.file_manager.list_image_names_with_path_directory(path)))

    def test_list_image_names_with_path_directory_return_a_empty_list_when_no_images_exist(self):
        
        folder="/empty"
        path = self.current_path + folder
        self.assertEquals(0, len(self.file_manager.list_image_names_with_path_directory(path)))

    def test_list_image_sizes_from_path_return_a_list_with_image_sizes(self):
        
        self.assertEquals([154844L, 8170L, 551980L, 154844L, 73695L, 27838L, 8170L, 45789L, 25612L], self.file_manager.list_image_sizes_from_path(self.current_path))

    def test_list_image_sizes_from_path_return_a_list_with_image_sizes_with_three_matching_files_and_one_different(self):
        
        folder = "/moreimages"
        path = self.current_path + folder
        self.assertEquals([154844L, 73695L, 27838L, 8170L, 45789L, 25612L], self.file_manager.list_image_sizes_from_path(path))

    def test_list_image_sizes_from_path_return_a_empty_list_when_no_images_exist(self):
        
        folder="/input/empty"
        path = self.current_path + folder
        self.assertEquals([], self.file_manager.list_image_sizes_from_path(path))

    def test_verify_path_directory_exists_when_user_insert_a_valid_path(self):
        
        self.assertEquals(self.current_path, self.file_manager.directory_exists(self.current_path))

    def test_verify_path_directory_exists_when_user_insert_an_invalid_path(self):
        
        self.assertEquals("This is an invalid path", self.file_manager.directory_exists("InvalidPath"))

    def test_verify_image_exist_when_user_insert_an_existing_image(self):
        
        folder = "/tank.png"
        path_image = self.current_path + folder
        self.assertTrue(self.file_manager.validate_type_of_image(path_image))	

    def test_verify_image_exist_when_user_insert_an_unexisting_image(self):
        
        image = "/92.jpg"
        path_image = self.current_path + image
        self.assertFalse(self.file_manager.validate_type_of_image(image))
    
    def test_verify_image_exist_when_user_insert_a_txt_file(self):
        
        txt_file = "/moreimages/readme.txt"
        path_file = self.current_path + txt_file
        self.assertFalse(self.file_manager.validate_type_of_image(path_file))



