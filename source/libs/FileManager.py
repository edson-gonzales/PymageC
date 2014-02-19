
import os

class FileManager():


    def get_current_path(self):
        """
        This method returns the current path directory

        Return:
        current_path.- String with the current path.
        """
        current_path = os.getcwd()
        return current_path

    def list_image_from_path(self, current_path):
        """
        This method lists all the image files of a specific path
        The list of the image files consider also the images within other directories
        Only the images with the follwoing extension are listed: .jpg   .png   .bmp

        Parameters:
        current_path .- Path directory to find all the images
        Return:
        list_image.- List with all the image names of a specific path
        """
        list_image = []
        for base, dirs, files in os.walk(current_path):
            for image in files:
                if (image.endswith(".jpg") == True or image.endswith(".png") == True 
                    or image.endswith(".bmp") == True):
                    
                    list_image.append(image)

        return list_image           
    
    def directory_exists(self, path_directory):
        """
        This method verify if a path directory given exists
        Parameters:
        path_directory.- String with a path directory
        """
        if os.path.isdir(path_directory):
            return path_directory
        else:
            return "This is an invalid path"

    def validate_type_of_image(self, image_file):
        """
        This method verify if a the image is supported by the application
        Parameters:
        image_file.- String with all the direction of an image file
                     Example:
                     G:\Pymage Mario\PYMAGE C\Tests\Input\920.jpg
        """
        if os.path.isfile(image_file):
            if (image_file.endswith(".jpg") or image_file.endswith(".bmp") 
                or image_file.endswith(".png")):
                return True
            else: 
                return False
        else:
            return False



#main = FileManager()
#path = "C:\Users\Mario Perez\Desktop\DevFundamentals\Final Project\PYMAGE C\Tests/input/moreimages"
#lista = main.list_image_from_path(path)
#print lista
    




