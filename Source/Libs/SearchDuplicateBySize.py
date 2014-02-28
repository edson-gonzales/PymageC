from constants import *
import os
import sys
from logger import LoggerManager 
sys.path.append("..")
from FileManager import FileManager
from SearchDuplicate import SearchDuplicate

class SearchDuplicateBySize(SearchDuplicate):
    def __init__(self):
        global loggerManager
        loggerManager =  LoggerManager("../source/log/")
    
    def search_duplicate(self, list_images):
        """
        This method search all the image sizes duplicatd an a given list.
        Parameters:
        list_images.- List of images sizes that belong a specific folder and sub folders
        Return:
        list_images_duplicated.- List with all the image sizes duplicated
        """
        seen = set()
        seen_add = seen.add
        seen_twice = set(x for x in list_images if x in seen or seen_add(x))
        list_images_duplicated = list(seen_twice)
        loggerManager.info("Search has finished succesfully")
        return list_images_duplicated

    def extract_entire_path_of_each_image_duplicated(self, list_images_duplicated, path):
        """
        This method returns the entire path directory of each image sent in the 
        'list_images_duplicated' list
        Parameters: 
        list_images_duplicated.- List with all the image sizes duplicated
        path.- Specific directory to extract the entire path of each image size duplicated 
               taking in account the subdirectories 
        """
        list_images_duplicated_with_paths = []
        for image_duplicated in list_images_duplicated:
            for base, dirs, files in os.walk(path):
                for image in files:
                    image_extension = image.split(".")[-1]
                    if image_extension in types:
                        image_name = base + "/" + image
                        size = os.path.getsize(image_name)
                        if (size == image_duplicated):
                            list_images_duplicated_with_paths.append(image_name)
        loggerManager.info("Paths were found extracted succesfully ")
        return list_images_duplicated_with_paths



