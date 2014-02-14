
import unittest
import sys
sys.path.append("../source/libs")
from FileManager import FileManager
import os

class FileManagerTest(unittest.TestCase):
    
    
    def setUp(self):
        
        self.current_path = os.getcwd()
        
    def test_aget_current_path_return_the_current_path(self):
    
        self.assertEquals(self.current_path, file_manager.get_current_path())

    def test_blist_image_from_path_return_a_list_with_images(self):
        
        self.assertEquals(["pregoneroOficial.jpg", "apple.bmp", "tank.png", "test.jpg", "programmer.jpg", "bmp.bmp", "linux.png"], file_manager.list_image_from_path(self.current_path))

    def test_clist_image_from_path_return_a_list_with_images_with_three_matching_files_and_one_different(self):
        
        folder = "/input/moreimages"
        path = self.current_path + folder
        self.assertEquals(["test.jpg", "programmer.jpg", "bmp.bmp", "linux.png"], file_manager.list_image_from_path(path))
    
    def test_dlist_image_from_path_return_a_empty_list_when_no_images_exist(self):
        
        folder="/input/empty"
        path = self.current_path + folder
        self.assertEquals([], file_manager.list_image_from_path(path))    

    def test_everify_path_directory_exists_when_user_insert_a_valid_path(self):
        
        self.assertEquals(self.current_path, file_manager.directory_exists(self.current_path))

    def test_fverify_path_directory_exists_when_user_insert_an_invalid_path(self):
        
        self.assertEquals("This is an invalid path",file_manager.directory_exists("InvalidPath"))

    def test_gverify_image_exist_when_user_insert_an_existing_image(self):
        
        folder = "/input/tank.png"
        path_image = self.current_path + folder
        self.assertTrue(file_manager.validate_type_of_image(path_image))	

    def test_hverify_image_exist_when_user_insert_an_unexisting_image(self):
        
        image = "/input/92.jpg"
        path_image = self.current_path + image
        self.assertFalse(file_manager.validate_type_of_image(image))
    
    def test_iverify_image_exist_when_user_insert_an_unexisting_image(self):
        
        txt_file = "/input/moreimages/readme.txt"
        path_file = self.current_path + txt_file
        self.assertFalse(file_manager.validate_type_of_image(path_file))

if __name__ == "__main__":
    file_manager= FileManager()
    unittest.main()


