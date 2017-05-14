#!/usr/bin/python3
from bottle import *
from jinja2 import Environment, FileSystemLoader
from web.controllers.navController import NavController
from web.controllers.imageController import ImageController
from web.controllers.textController import TextController
from services.imageService import ImageService
from services.hocrService import HocrService

class WebCorrector:

    def __init__(self):
        self.host = 'localhost'
        self.port = '8080'
        self.app = Bottle()
        self.env = self.init_environment()
        self.controllers = self.init_controllers()
        self.init_routes()

    def init_routes(self):
        self.app.route('/web/assets/:p_file#.+#', name='static', callback=self.return_resource)
        self.app.route('/pages', method="GET", callback=self.controllers['navController'].home)
        self.app.route('/images/<id>', method="GET", callback=self.controllers['imageController'].get_image)
        self.app.route('/images/last/id', method="GET", callback=self.controllers['imageController'].get_last_id)
        self.app.route('/texts/<id>', method="GET", callback=self.controllers['textController'].get_text)
        self.app.route('/saves/<id>', method="POST", callback=self.controllers['textController'].save_text)

    def init_controllers(self):
        self.image_service = ImageService()
        self.hocr_service = HocrService()
        controllers = {
            'imageController': ImageController(self.image_service),
            'navController': NavController(self.env),
            'textController': TextController(self.hocr_service)
        }
        return controllers

    def init_environment(self):
        env = Environment(loader=FileSystemLoader(searchpath='jabiru/src/web/views/'),
                            extensions=['pyjade.ext.jinja.PyJadeExtension'])
        return env

    def return_resource(self, p_file):
        return static_file(p_file, root='jabiru/src/web/assets')


    def run_app(self):
        self.app.run(host=self.host, port=self.port, quiet=False, debug=True)

#forma de llamar a esta clase:

app = WebCorrector()
app.run_app()
