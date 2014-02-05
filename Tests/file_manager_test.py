import unittest
import sys
sys.path.append("../Source/Libs")
from FileManager import FileManager
import os

class FileManagerTest(unittest.TestCase):
    
    
    def setUp(self):
        
        self.current_path = os.getcwd()
        
    def test_aget_current_path_return_the_current_path(self):
    
        self.assertEquals(self.current_path, file_manager.get_current_path())

    def test_blist_image_from_path_return_a_list_with_images(self):
        
        self.assertEquals(["920.jpg", "pregoneroOficial.jpg", "test.jpg", "test2.jpg", "programmer.jpg"], file_manager.list_image_from_path(self.current_path))

    def test_clist_image_from_path_return_a_list_with_images_with_three_matching_files_and_one_different(self):
        
        folder = "/Input/MoreImages"
        path = self.current_path + folder
        self.assertEquals(["test.jpg", "test2.jpg", "programmer.jpg"], file_manager.list_image_from_path(path))
    
    def test_dlist_image_from_path_return_a_empty_list_when_no_images_exist(self):
        
        folder="/Input/empty"
        path = self.current_path + folder
        self.assertEquals([], file_manager.list_image_from_path(path))    

    def test_everify_path_directory_exists_when_user_insert_a_valid_path(self):
        
        self.assertEquals(self.current_path, file_manager.verify_path_directory_exists(self.current_path))

    def test_fverify_path_directory_exists_when_user_insert_an_invalid_path(self):
        
        self.assertEquals("This is an invalid path",file_manager.verify_path_directory_exists("InvalidPath"))

    def test_gverify_image_exist_when_user_insert_an_existing_image(self):
        
        folder = "/Input/920.jpg"
        path_image = self.current_path + folder
        self.assertEquals(path_image ,file_manager.verify_image_exist(path_image))		

    def test_hverify_image_exist_when_user_insert_an_unexisting_image(self):
        
        image = "G:\Pymage Mario\PYMAGE C\Tests\Input\92.jpg"
        self.assertEquals("This image doesnt exist" ,file_manager.verify_image_exist(image))
    
    def test_iverify_image_exist_when_user_insert_an_unexisting_image(self):
        
        txt_file = "/Input/MoreImages/readme.txt"
        path_file = self.current_path + txt_file
        self.assertEquals("This is not an image file", file_manager.verify_image_exist(path_file))

if __name__ == "__main__":
    file_manager= FileManager()
    unittest.main()

    