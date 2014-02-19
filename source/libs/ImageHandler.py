from PIL import Image
import os
import sys
sys.path.append("..")
from FileManager import FileManager

class ImageHandler():
	
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
        except:
            print "Error while processing the image"
        

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
        except:
            print "Error while processing the image"


#list = ["H:\920.jpg",90,"H:\990.jpg"]
#main = ImageHandler()
#main.rotate_image(list)