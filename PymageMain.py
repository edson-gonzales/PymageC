import os
import sys
sys.path.append("source/libs")
from PIL import Image
from FileManager import FileManager
from ImageHandler import ImageHandler

class PymageMain():
    
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
    
    def read_directory_from_user(self):
        """
        This method read a directory path inserted by the user.
        Return:
        path_directory.- String with the value inserted by the user
        """
        path_directory = raw_input("Insert a path directory to search images:")
        path_directory = str(path_directory)
        return path_directory

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
                  If the number inserted is out of the valid range, the method returns 9999
        """
        image_handler = ImageHandler()
        msg_to_display = "Insert the number of degrees to rotate the image: "
        degrees = self.read_value_from_user(msg_to_display)
        degrees = int(degrees)
        if image_handler.validate_degrees_inserted(degrees) == True:
            return degrees
        else:
            return 9999

    def read_name_to_save_image_rotate(self):
        """
        This method reads from the user the name for the new image.
        A new image is created when the user rotates an image file, keeping the original image.
        """
        msg_to_display = """Insert the path directory with the new name of the image file.
        (E.g. G:\Pymage Mario\PYMAGE C\Tests\Input\New_image.jpg):  """
        image_name = self.read_value_from_user(msg_to_display)
        image_name = str(image_name)
        return image_name

    def read_format_to_export_an_image(self):
        """
        This method reads the format to export an image file from one format to another 

        Return:
        new_format.- String with the new format to convert the image
        """
        image_handler = ImageHandler()
        msg_to_display = "Insert the format to export an image file from one format to another: "
        new_format = self.read_value_from_user(msg_to_display)
        if (image_handler.validate_format_inserted(new_format) == True):
            return new_format
        else:
            return "Incorrect format"

    def read_all_values_to_rotate(self):
        """
        This method read all the data required by the final user to rotate an image
        Return:
        input_values.- List with all the inputs inserted by the user
                       [Image path,  degrees, New name of the image]
                       If some value inserted is invalid, the method returns a empty list
        """
        file_manager = FileManager()
        input_values = []
        image_path = self.read_image_path()
        if (file_manager.validate_type_of_image(image_path) == True):
            degrees = self.read_degrees_to_rotate_image()
            if (degrees != 9999):
                new_image_name = self.read_name_to_save_image_rotate()
                input_values = [image_path, degrees, new_image_name]
                return input_values
            else:
                return input_values
        else:
            return input_values


    def read_all_values_to_export_an_image_file_to_another_format(self):
        """
        This method read all the data required by the final user to export an image
        to another format.
        The formats that are supported by the application are: jpg, bmp and png

        Return: List with all the inputs inserted by the user
                [Image path,  new format]
                If some value inserted is invalid, the method returns a empty list
        """
        file_manager = FileManager()
        input_values = []
        image_path = self.read_image_path()
        if (file_manager.validate_type_of_image(image_path) == True):
            new_format = self.read_format_to_export_an_image()
            if (new_format != "Incorrect format"):
                input_values = [image_path, new_format]
                return input_values
            else:
                return input_values
        else:
            return input_values



main = PymageMain()        
image_handler = ImageHandler()
#result = main.read_all_values_to_rotate()
#if (len(result) != 0):
#    print result
#    image = image_handler.rotate_image(result)
#    main.save_image_file(image, result[2])

#else:
#    print "False"


input_values = main.read_all_values_to_export_an_image_file_to_another_format()
if (len (input_values) != 0):
#    print input_values
    image_handler.export_an_image_file_to_another_format(input_values)
else:
    print "False"
