
import os

class FileManager():


    def get_current_path(self):
        """
        This method returns the current path directory

        Return:
        current_path.- String with the current path.
        """
        current_path=os.getcwd()
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

    def read_directory_from_user(self):
        """
        This method read a directory path inserted by the user.
        Return:
        path_directory.- String with the value inserted by the user
        """
        path_directory = raw_input("Insert a path directory to search images:")
        path_directory = str(path_directory)
        return path_directory
    
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

    def image_exists(self, image_file):
        """
        This method verify if a image file exists
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
                return "This is not an image file"
        else:
            return "This image doesnt exist"




    




