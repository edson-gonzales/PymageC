from constants import *
import os
from logger import LoggerManager 

class FileManager():
    def __init__(self):
        global loggerManager
        loggerManager =  LoggerManager("../source/log/")

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
                image_extension = image.split(".")[-1]
                if image_extension in types:
                    list_image.append(image)
        loggerManager.info("List from path operation has finished succesfully")
        return list_image           
    
    def list_image_names_with_path_directory(self, current_path):
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
                image_extension = image.split(".")[-1]
                if image_extension in types:    
                    image_name_with_path = base + "/" + image
                    list_image.append(image_name_with_path)
        loggerManager.info("List from name operation has finished succesfully")
        return list_image

    def list_image_sizes_from_path(self, current_path):
        """
        This method lists all the image sizes of a specific path
        The list of the image sizes consider also the images within other directories
        Only the images with the follwoing extension are listed: .jpg   .png   .bmp

        Parameters:
        current_path .- Path directory to find all the images
        Return:
        list_image_size.- List with all the image sizes of a specific path
        """
        list_image_sizes = []
        for base, dirs, files in os.walk(current_path):
            for image in files:
                image_extension = image.split(".")[-1]
                if image_extension in types:
                    image_name = base + "/" + image
                    size = os.path.getsize(image_name)
                    list_image_sizes.append(size)
        loggerManager.info("List by size operation has finished succesfully")
        return list_image_sizes

    def directory_exists(self, path_directory):
        """
        This method verify if a path directory given exists
        Parameters:
        path_directory.- String with a path directory
        """
        if os.path.isdir(path_directory):
            return path_directory
        else:
            loggerManager.error("This is an invalid path")        

  

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
                loggerManager.warning("Image is not supported")                
                return False
        else:
            loggerManager.warning("Image is not supported")
            return False



