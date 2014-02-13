import os
import sys
sys.path.append("source/libs")
from PIL import Image
from FileManager import FileManager
from ImageHandler import ImageHandler

class PymageMain():
    
    def rotate_image(self, input_values):
        """
        This method rotate an image file the number of degrees received.
        A new image is created and saved
        Parameter:
        input_values.- List with all the inputs inserted by the user
                       [Image path,  degrees, New name of the image]
        """
        
        image_open = Image.open(input_values[0])
        image_rotate = image_open.rotate(input_values[1])
        image_rotate.save(input_values[2])

    def export_an_image_file_to_another_format(self, input_values):
        """
        This method export an image file from one format to another.
        The formats that are supported by the application are: jpg, bmp and png
        Parameter:
        input_values.- List with all the inputs inserted by the user
                       [Image path,  new format]
        """   

        new_image = os.path.splitext(input_values[0])[0] + "." + input_values[1]
        Image.open(input_values[0]).save(new_image)





#image_handler = ImageHandler()
#main = PymageMain()
#input_values = image_handler.read_all_values_to_rotate()
#if (input_values != False):
#    main.rotate_image(input_values)
#else:
#    print "The number of degrees inserted is wrong. It has to be between -360 and 360 or \n"
#    print "This is not an image file or the image doesnt exist"

#input_values = image_handler.read_all_values_to_export_an_image_file_to_another_format()
#if (input_values != False):
#    main.export_an_image_file_to_another_format(input_values)
#else:
    #print "The number of degrees inserted is wrong. It has to be between -360 and 360 or \n"
    #print "This is not an image file or the image doesnt exist"
#    print "This is not an image file or the image doesnt exist"
#    print "The format inserted is incorrect or is not supported"

