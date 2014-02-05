
import os

class FileManager():


    def get_current_path(self):
        """
        This method returns the current path directory

        Parameters:
        None
        """
        current_path=os.getcwd()
        return current_path

    def list_image_from_path(self, current_path):
        """
        This method lists all the image files os a specific path
        The list of the image files consider also the images within other directories
        Only the images with the follwoing extension are listed: .jpg   .png   .bmp

        Parameters"
        current_path .- Path directory to find all the images
        """
        list_image = []
        for base, dirs, files in os.walk(current_path):
            #print base
            for image in files:
                if (image.endswith(".jpg") == True or image.endswith(".png") == True 
                    or image.endswith(".bmp") == True):
                    #print image
                    list_image.append(image)

        return list_image           

    def read_directory_from_user(self):
        """
        This method read a directory path inserted by the user.
        Parameters:
        None
        """
        path_directory = raw_input("Insert a path directory to search images:")
        path_directory = str(path_directory)
        return path_directory
    
    def verify_path_directory_exists(self, path_directory):
        """
        This method verify id a path directory given exists
        Parameters:
        path_directory.- String with a path directory
        """
        if os.path.isdir(path_directory):
            return path_directory
        else:
            return "This is an invalid path"

    def verify_image_exist(self, image_file):
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
                return image_file
            else: 
                return "This is not an image file"
        else:
            return "This image doesnt exist"




    




