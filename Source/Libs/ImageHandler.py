from PIL import Image
import os
import sys
sys.path.append("..")
from FileManager import FileManager


class ImageHandler():

    def read_value_from_user(self, msg_to_display):
        """
        This method displays a custom message to the final user and reads
        a variable inserted by the user
        Parameters:
        msg_to_display.- String with the message to be displayed to the final user 

        Return:
        value_inserted.- Return the value typed by the final user
        """
        value_inserted = raw_input(msg_to_display)
        return value_inserted
    
    def read_image_path(self):
    	"""
    	This method reads the image path that will be processed

    	Return:
    	image_path.- Path directory of the image that will be processed
    	"""
        msg_to_display = "Insert the path directory of the image that will be processed: "
        image_path = self.read_value_from_user(msg_to_display)
        return str(image_path)


    def read_degrees_to_rotate_image(self):
        """
        This method reads from the user the number of degrees to rotates an image file
        Evaluate the number inserted and returns the number of degrees if it is correct
        otherwise print an error message

        Return:
        degrees.- Number of degrees to rotate the image
        """
        msg_to_display = "Insert the number of degrees to rotate the image: "
        degrees = self.read_value_from_user(msg_to_display)
        degrees = int(degrees)
        if self.validate_degrees_inserted(degrees) == True:
            return degrees
        else:
            return False 

    def read_name_to_save_image_rotate(self):
        """
        This method reads from the user the name for the new image.
        A new image is created when the user rotates an image file, keeping the original image.
        """
        msg_to_display = "Insert the path directory with the new name of the image file. \n" +
                         " (E.g. G:\Pymage Mario\PYMAGE C\Tests\Input\New_image.jpg): "
        image_name = self.read_value_from_user(msg_to_display)
        image_name = str(image_name)
        return image_name

    def show_image(self, image):
        """
        This methos displays an image file

        Parameter:
        image.-  String with path directory of the image to be displayed
        """

        try:
            image.show()
        except:
            print "The image cannot be displayed!"
	
    def validate_degrees_inserted(self, degrees):
        """
        This method evaluate the number of degrees to rotates an image
        Retunt True when the number received is between -360 and 360
        otherwise returns False 
        Parameter:
        degrees .- Integer with the number to be evaluated
        """
        if (degrees <= 360 and degrees >= -360):
            return True
        else: 
            return False

    def read_format_to_export_an_image(self):
        """
        This method reads the format to export an image file from one format to another 

        Return:
        new_format.- String with the new format to convert the image
        """
        msg_to_display = "Insert the format to export an image file from one format to another: "
        new_format = self.read_value_from_user(msg_to_display)
        if (self.validate_format_inserted(new_format) == True):
            return new_format
        else:
            return False

    def validate_format_inserted(self, new_format):
        """
        This method validate the format inserted by the user.
        The application support .jpg, .bmp and .png
        Return:
        True.- When the format is correct
        False.- When the format is incorrect or is not supported
        """
        if (new_format == 'jpg' or new_format == 'bmp' or new_format == 'png'):
            return True
        else:
            return False

    def read_all_values_to_rotate(self):
        """
        This method read all the data required by the final user to rotate an image
        Return:
        input_values.- List with all the inputs inserted by the user
                       [Image path,  degrees, New name of the image]
        """
        file_manager = FileManager()
        image_path = self.read_image_path()
        if (file_manager.image_exists(image_path) == True):
            degrees = self.read_degrees_to_rotate_image()
            if (degrees != False):
                new_image_name = self.read_name_to_save_image_rotate()
                input_values = [image_path, degrees, new_image_name]
                return input_values
            else:
                return False
        else:
            return False


    def read_all_values_to_export_an_image_file_to_another_format(self):
        """
        This method read all the data required by the final user to export an image
        to another format.
        The formats that are supported by the application are: jpg, bmp and png

        Return: List with all the inputs inserted by the user
                [Image path,  new format]
        """
        file_manager = FileManager()
        image_path = self.read_image_path()
        if (file_manager.image_exists(image_path) == True):
            new_format = self.read_format_to_export_an_image()
            if (new_format != False):
                input_values = [image_path, new_format]
                return input_values
            else:
                return False
        else:
            return False