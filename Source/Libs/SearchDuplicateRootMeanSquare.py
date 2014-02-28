
import os
from logger import LoggerManager 
from PIL import Image
from PIL import ImageChops
import math, operator
from constants import *
from FileManager import FileManager

class SearchDuplicateRootMeanSquare():
    def __init__(self):
        global loggerManager
        loggerManager =  LoggerManager("../source/log/")

    def compare_all_images(self, list_images, path_directory):
        """
        This method returns the entire path directory of each image duplicated
        using the root maean square alghoritm.
        Compare all the images received in a list (list_images) with all the images
        that belong path directory (path_directory) received and sub directories
        Parameters: 
        list_images.- List with all the image path directories
        path_directory.- String with a path directory to compare the images 
        Return:
        Result.- List with all the images duplicated
        """
    	result = []
        auxiliar = []
    	for image_duplicated in list_images:   
            for base, dirs, files in os.walk(path_directory):
                for image in files:                    
                    image_extension = image.split(".")[-1]
                    if image_extension in types:
                        image_name = base + "/" + image
                        if image_name not in auxiliar:
                            if (image_duplicated != image_name):
                                image_open1 = Image.open(image_duplicated)
                                image_open2 = Image.open(image_name)
                                rms = self.root_maean_square(image_open1, image_open2)
                                if (rms >= 570 and rms <= 574):
                                    result.append(image_name)
                                    result.append(image_duplicated)
                                    auxiliar.append(image_duplicated)
        loggerManager.info("Search has finished succesfully")
        return result

    def root_maean_square(self, image1, image2):
        """
        This method received two images and compare both using the root main square alghoritm
        Parameters:
        image1 .- Image object with the first image to compare
        image2 .- Image object with the second image to compare 
        Return:
        rms.- Result of the comparision of both images received.
        """
        diff = ImageChops.difference(image1, image2)
        h = diff.histogram()
        sq = (value * (idx ** 2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares / float (image1.size[0] * image1.size[1]))
        loggerManager.info("Comparision operation has finished successfully")
        return rms

