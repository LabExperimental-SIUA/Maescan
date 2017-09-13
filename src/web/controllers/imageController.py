from jpegtran import JPEGImage
from bottle import HTTPResponse
import os
import glob


class ImageController:

    def __init__(self, image_service):
        self.image_service = image_service

    def get_image(self, p_id):
        # Variable para la ruta al directorio
        # este va a ser el path de la imagen
        path = environ["LS_PROJECT_PATH"]+'/processed/'
        
        l = glob.glob(path + '*.tif')
        l.sort()
        
        image_name = l[int(p_id)]
        
        temp = image_name.split('.')
        new_image = temp[0]
        new_image = new_image + ".jpg"
        
        if not os.path.isfile(new_image):
            self.image_service.convert_image(p_id)
        
        headers = {
            'Content-Type': 'image/jpg'
        }
        image = JPEGImage(new_image)
        body = image.as_blob()
        return HTTPResponse(body, **headers)

    def get_last_id(self):
        last_line = 0
        infile = open(environ["LS_PROJECT_PATH"]+'/.pics.ls', 'r')

        for line in infile:
            last_line += 1
             
        infile.close()

        return {'last_id': last_line}
