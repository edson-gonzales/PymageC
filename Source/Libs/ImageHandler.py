from constants import *
from PIL import Image
import os
import sys

from logger import LoggerManager 
sys.path.append("..")
from FileManager import FileManager

class ImageHandler():
    def __init__(self):
        global loggerManager
        loggerManager =  LoggerManager("../source/log/")
	
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
            loggerManager.error("Degrees have incorrect Values ") 
            return False
    
    def validate_format_inserted(self, new_format):
        """
        This method validate the format inserted by the user.
        The application support .jpg, .bmp and .png
        Return:
        True.- When the format is correct
        False.- When the format is incorrect or is not supported
        """
        if new_format in types:
            return True
        else:
            loggerManager.error("Format is incorrect or is not supported")
            return False

    def rotate_image(self, input_values):
        """
        This method rotate an image file the number of degrees received.
        A new image is created and saved
        Parameter:
        input_values.- List with all the inputs inserted by the user
                       [Image path,  degrees, New name of the image]
        """
        try:
            image_open = Image.open(input_values[0])
            image_rotate = image_open.rotate(input_values[1])
            image_rotate.save(input_values[2])
        except Exception, e:
            loggerManager.error("Error while processing the image: {0}".format(e.message))        

    def export_an_image_file_to_another_format(self, input_values):
        """
        This method export an image file from one format to another.
        The formats that are supported by the application are: jpg, bmp and png
        Parameter:
        input_values.- List with all the inputs inserted by the user
                       [Image path,  new format]
        """   
        
        try:    
            new_image = os.path.splitext(input_values[0])[0] + "." + input_values[1]
            Image.open(input_values[0]).save(new_image)
        except Exception, e:
            loggerManager.error("Error while processing the image: {0}".format(e.message))

    def resize_image(self, image_path, new_width, new_height,new_name):
        """
        This method resize an image giving the image path and new dimentions
        width and height.
        Parameters:
        image_path.- String with path directory of the image to be resized
        new_width.- Integer for width in pixels
        new_height.- Integer for height in pixels
        new_name.- Integer for height in pixels
        Return: An object image 
        """
        if(new_width >= 0 and new_height >= 0):
            image_open = Image.open(image_path)
            image_resize = image_open.resize((new_width, new_height), Image.ANTIALIAS)
            image_resize.save(new_name)
            return image_resize
        else:
            loggerManager.error("Values for resize must not be negatives")
        
    def obtain_size(self, image):
        """
        This method obtains height and width of an image 
        Parameter:
        image .- Image to obtains dimentions
        return.- (with, height)
        """
        try:
            return image.size
        except Exception, e:
            loggerManager.error("Values for image size are incorrect: {0}".format(e.message))
            

