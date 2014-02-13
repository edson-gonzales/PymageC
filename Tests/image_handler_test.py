import unittest
import sys
import os
sys.path.append("../source/libs")
from ImageHandler import ImageHandler

class ImageManagerTest(unittest.TestCase):
    
    def setUp(self):
        
        self.current_path = os.getcwd()

    def test_validate_degrees_inserted_sending_number_in_the_valid_range(self):
        self.assertTrue(image_handler.validate_degrees_inserted(180), "180 degrees should be permitted")

    def test_validate_degrees_inserted_sending_number_outside_the_lower_limit(self):
        self.assertFalse(image_handler.validate_degrees_inserted(-361), "There is an issue in the lower limit")
    
    def test_validate_degrees_inserted_sending_number_outside_the_upper_limit(self):
        self.assertFalse(image_handler.validate_degrees_inserted(361), "There is an issue in the upper limit")

    def test_read_value_from_user_when_final_user_insert_a_string(self):
        pass

    def test_read_value_from_user_returns_the_same_string_inserted_by_final_user(self):
        pass

    def test_read_image_path_returns_the_same_string_inserted_by_final_user(self):
        pass

    def test_read_degrees_to_rotate_image_returns_the_number_of_degrees_when_value_inserted_is_correct(self):
        pass

    def test_read_degrees_to_rotate_image_returns_false_when_final_user_insert_value_out_of_limits(self):
        pass

    def test_read_name_to_save_image_rotate_returns_the_same_string_inserted_by_final_user(self):
        pass

    def test_validate_format_inserted_returns_true_when_the_format_inserted_is_supported(self):
        self.assertTrue(image_handler.validate_format_inserted("png"), "The format inserted is is incorrect on is not supported")
        self.assertTrue(image_handler.validate_format_inserted("jpg"), "The format inserted is is incorrect on is not supported")
        self.assertTrue(image_handler.validate_format_inserted("bmp"), "The format inserted is is incorrect on is not supported")

    def test_validate_format_inserted_returns_false_when_insert_a_format_not_supported(self):
        self.assertFalse(image_handler.validate_format_inserted("ico"), "This format is not supported")




if __name__ == "__main__":
    image_handler= ImageHandler()
    unittest.main()