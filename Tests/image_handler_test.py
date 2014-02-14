import unittest
import sys
import os
sys.path.append("../source/libs")
from ImageHandler import ImageHandler
from FileManager import FileManager
from PymageMain import PymageMain

class ImageManagerTest(unittest.TestCase):
    
    def setUp(self):
        
        self.current_path = os.getcwd()

    def test_validate_degrees_inserted_sending_number_in_the_valid_range(self):
        self.assertTrue(image_handler.validate_degrees_inserted(180), "180 degrees should be permitted")

    def test_validate_degrees_inserted_sending_number_outside_the_lower_limit(self):
        self.assertFalse(image_handler.validate_degrees_inserted(-361), "There is an issue in the lower limit")
    
    def test_validate_degrees_inserted_sending_number_outside_the_upper_limit(self):
        self.assertFalse(image_handler.validate_degrees_inserted(361), "There is an issue in the upper limit")

    def test_validate_format_inserted_returns_true_when_the_format_inserted_is_supported(self):
        self.assertTrue(image_handler.validate_format_inserted("png"), "The format inserted is is incorrect on is not supported")
        self.assertTrue(image_handler.validate_format_inserted("jpg"), "The format inserted is is incorrect on is not supported")
        self.assertTrue(image_handler.validate_format_inserted("bmp"), "The format inserted is is incorrect on is not supported")

    def test_validate_format_inserted_returns_false_when_insert_a_format_not_supported(self):
        self.assertFalse(image_handler.validate_format_inserted("ico"), "This format is not supported")

    def test_rotate_image_creates_new_image_file_with_image_rotated_using_jpg_type(self):
        image = "/input/pregoneroOficial.jpg"
        image_path = self.current_path + image
        degrees = 90
        new_name = "/input/pregoneroOficial_rotate.jpg"
        new_name_jpg_path = self.current_path + new_name
        input_values = [image_path, degrees, new_name_jpg_path]
        image_handler.rotate_image(input_values)
        self.assertTrue(file_manager.validate_type_of_image(new_name_jpg_path), "A new image was not created")
        os.remove(new_name_jpg_path)

    def test_rotate_image_creates_new_image_file_with_image_rotated_using_png_type(self):
        image = "/input/tank.png"
        image_path = self.current_path + image
        degrees = 90
        new_name = "/input/tank_rotate.png"
        new_name_png_path = self.current_path + new_name
        input_values = [image_path, degrees, new_name_png_path]
        image_handler.rotate_image(input_values)
        self.assertTrue(file_manager.validate_type_of_image(new_name_png_path), "A new image was not created")
        os.remove(new_name_png_path)

    def test_rotate_image_creates_new_image_file_with_image_rotated_using_bmp_type(self):
        image = "/input/apple.bmp"
        image_path = self.current_path + image
        degrees = 90
        new_name = "/input/apple_rotate.bmp"
        new_name_bmp_path = self.current_path + new_name
        input_values = [image_path, degrees, new_name_bmp_path]
        image_handler.rotate_image(input_values)
        self.assertTrue(file_manager.validate_type_of_image(new_name_bmp_path), "A new image was not created")
        os.remove(new_name_bmp_path)

    def test_export_a_jpg_image_file_to_png_image_file(self):
        image = "/input/pregoneroOficial.jpg"
        image_path = self.current_path + image
        new_format = "png"
        new_image = self.current_path + "/input/pregoneroOficial.png"
        input_values = [image_path, new_format]
        image_handler.export_an_image_file_to_another_format(input_values)
        self.assertTrue(file_manager.validate_type_of_image(new_image), "The image was not exported to another format")
        os.remove(new_image)    

    def test_export_a_jpg_image_file_to_bmp_image_file(self):
        image = "/input/pregoneroOficial.jpg"
        image_path = self.current_path + image
        new_format = "bmp"
        new_image = self.current_path + "/input/pregoneroOficial.bmp"
        input_values = [image_path, new_format]
        image_handler.export_an_image_file_to_another_format(input_values)
        self.assertTrue(file_manager.validate_type_of_image(new_image), "The image was not exported to another format")
        os.remove(new_image) 

    def test_export_a_png_image_file_to_bmp_image_file(self):
        image = "/input/tank.png"
        image_path = self.current_path + image
        new_format = "bmp"
        new_image = self.current_path + "/input/tank.bmp"
        input_values = [image_path, new_format]
        image_handler.export_an_image_file_to_another_format(input_values)
        self.assertTrue(file_manager.validate_type_of_image(new_image), "The image was not exported to another format")
        os.remove(new_image) 

    def test_export_a_bmp_image_file_to_jpg_image_file(self):
        image = "/input/apple.bmp"
        image_path = self.current_path + image
        new_format = "jpg"
        new_image = self.current_path + "/input/apple.jpg"
        input_values = [image_path, new_format]
        image_handler.export_an_image_file_to_another_format(input_values)
        self.assertTrue(file_manager.validate_type_of_image(new_image), "The image was not exported to another format")
        os.remove(new_image)

if __name__ == "__main__":
    image_handler = ImageHandler()
    file_manager = FileManager()
    pymage_main = PymageMain()
    unittest.main()