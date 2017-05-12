from jpegtran import JPEGImage 
import os
class ImageService:
    def __init__(self):
        pass

    def convert_image(self, image):
        temp = image.split('.')
        new_image = temp[0]
        new_image = new_image + ".jpg"
        os.system("convert "+image+" "+new_image)   
        
