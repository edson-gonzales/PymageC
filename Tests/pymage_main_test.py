import unittest
import sys
import os
sys.path.append("../source/libs")
sys.path.append("../")
from ImageHandler import ImageHandler
from FileManager import FileManager
from PymageMain import PymageMain

class PymageMainTest(unittest.TestCase):
    
    def setUp(self):
        self.current_path = os.getcwd()
    
    def test_rotate_image_creates_new_image_file_with_image_rotated_using_jpg_type(self):
        image = "/input/pregoneroOficial.jpg"
        image_path = self.current_path + image
        degrees = 90
        new_name = "/input/pregoneroOficial_rotate.jpg"
        new_name_jpg_path = self.current_path + new_name
        input_values = [image_path, degrees, new_name_jpg_path]
        pymage_main.rotate_image(input_values)
        self.assertTrue(file_manager.image_exists(new_name_jpg_path), "A new image was not created")
        os.remove(new_name_jpg_path)

    def test_rotate_image_creates_new_image_file_with_image_rotated_using_png_type(self):
        image = "/input/tank.png"
        image_path = self.current_path + image
        degrees = 90
        new_name = "/input/tank_rotate.png"
        new_name_png_path = self.current_path + new_name
        input_values = [image_path, degrees, new_name_png_path]
        pymage_main.rotate_image(input_values)
        self.assertTrue(file_manager.image_exists(new_name_png_path), "A new image was not created")
        os.remove(new_name_png_path)

    def test_rotate_image_creates_new_image_file_with_image_rotated_using_bmp_type(self):
        image = "/input/apple.bmp"
        image_path = self.current_path + image
        degrees = 90
        new_name = "/input/apple_rotate.bmp"
        new_name_bmp_path = self.current_path + new_name
        input_values = [image_path, degrees, new_name_bmp_path]
        pymage_main.rotate_image(input_values)
        self.assertTrue(file_manager.image_exists(new_name_bmp_path), "A new image was not created")
        os.remove(new_name_bmp_path)
    
    def test_export_a_jpg_image_file_to_png_image_file(self):
        image = "/input/pregoneroOficial.jpg"
        image_path = self.current_path + image
        new_format = "png"
        new_image = self.current_path + "/input/pregoneroOficial.png"
        input_values = [image_path, new_format]
        pymage_main.export_an_image_file_to_another_format(input_values)
        self.assertTrue(file_manager.image_exists(new_image), "The image was not exported to another format")
        os.remove(new_image)    

    def test_export_a_jpg_image_file_to_bmp_image_file(self):
        image = "/input/pregoneroOficial.jpg"
        image_path = self.current_path + image
        new_format = "bmp"
        new_image = self.current_path + "/input/pregoneroOficial.bmp"
        input_values = [image_path, new_format]
        pymage_main.export_an_image_file_to_another_format(input_values)
        self.assertTrue(file_manager.image_exists(new_image), "The image was not exported to another format")
        os.remove(new_image) 

    def test_export_a_png_image_file_to_bmp_image_file(self):
        image = "/input/tank.png"
        image_path = self.current_path + image
        new_format = "bmp"
        new_image = self.current_path + "/input/tank.bmp"
        input_values = [image_path, new_format]
        pymage_main.export_an_image_file_to_another_format(input_values)
        self.assertTrue(file_manager.image_exists(new_image), "The image was not exported to another format")
        os.remove(new_image) 

    def test_export_a_bmp_image_file_to_jpg_image_file(self):
        image = "/input/apple.bmp"
        image_path = self.current_path + image
        new_format = "jpg"
        new_image = self.current_path + "/input/apple.jpg"
        input_values = [image_path, new_format]
        pymage_main.export_an_image_file_to_another_format(input_values)
        self.assertTrue(file_manager.image_exists(new_image), "The image was not exported to another format")
        os.remove(new_image)

if __name__ == "__main__":
    image_handler = ImageHandler()
    file_manager = FileManager()
    pymage_main = PymageMain()
    unittest.main()