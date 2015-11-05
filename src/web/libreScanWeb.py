from gettext import translation
from bottle import *
from services.cameraService import CameraService
from services.mailService import MailService
from services.projectService import ProjectService
from services.queueService import QueueService
from jinja2 import Environment, FileSystemLoader
from web.controllers.languageController import LanguageController
from web.controllers.mailController import MailController
from web.controllers.navigationController import NavigationController
from web.controllers.cameraController import CameraController
from web.controllers.projectController import ProjectController
from web.i18n.PoParser import PoParser


class LibreScanWeb:

    def __init__(self):
        self.host = '0.0.0.0'
        self.port = '8180'
        self.app = Bottle()
        self.default_language = 'spa'
        self.env = self.init_environment()
        self.controllers = self.init_controllers()
        self.init_routes()

    def init_environment(self):
        env = Environment(loader=FileSystemLoader(searchpath='views/'),
                            extensions=['pyjade.ext.jinja.PyJadeExtension', 'jinja2.ext.i18n'])
        translations = translation(domain='messages', localedir='./i18n/locale', languages=[self.default_language])
        env.install_gettext_translations(translations)
        return env

    def init_routes(self):
        self._init_camera_routes()
        self._init_mail_routes()
        self._init_navigation_routes()
        self.app.route('/assets/:p_file#.+#', name='static', callback=self.return_resource)
        self.app.route('/language/<lang>', method="GET", callback=self.controllers['language'].change_language)
        self.init_project_routes()

        # The other routes would go here.

    def _init_navigation_routes(self):
        self.app.route('/', method="GET", callback=self.controllers['navigation'].home)
        self.app.route('/scan', method="GET", callback=self.controllers['navigation'].scan)
        self.app.route('/about', method="GET", callback=self.controllers['navigation'].about)
        self.app.route('/contact', method="GET", callback=self.controllers['navigation'].contact)

    def init_project_routes(self):
        self.app.route('/project/<id>/config', method="GET", callback=self.controllers['project'].get_config)
        self.app.route('/project', method="POST", callback=self.controllers['project'].create)
        self.app.route('/project/new', method="GET", callback=self.controllers['project'].new)
        self.app.route('/project/load', method="GET", callback=self.controllers['project'].load)

    def _init_camera_routes(self):
        self.app.route('/photo', method="POST", callback=self.controllers['camera'].create)  # Route to handle shoot.
        self.app.route('/photo', method="PUT", callback=self.controllers['camera'].update)  # Route to handle recapture.
        self.app.route('/photo', method="DELETE", callback=self.controllers['camera'].delete)  # Route to handle delete.
        self.app.route('/photo', method="GET", callback=self.controllers['camera'].get)  # Route to handle get photo.

    def _init_mail_routes(self):
        self.app.route('/mail', method="GET", callback=self.controllers['mail'].create)

    def _init_navigation_routes(self):
        self.app.route('/', method="GET", callback=self.controllers['navigation'].home)
        self.app.route('/scan', method="GET", callback=self.controllers['navigation'].scan)
        self.app.route('/about', method="GET", callback=self.controllers['navigation'].about)
        self.app.route('/contact', method="GET", callback=self.controllers['navigation'].contact)
        self.app.route('/outputPreview', method="GET", callback=self.controllers['navigation'].output_preview)

    def init_controllers(self):
        camera_service = CameraService()
        mail_service = MailService()
        project_service = ProjectService()
        queue_service = QueueService()
        controllers = {
            'navigation': NavigationController(self.env),
            'camera': CameraController(self.env, camera_service, queue_service),
            'project': ProjectController(self.env, project_service),
            'mail': MailController(self.env, mail_service),
            'language': LanguageController(self.env)
        }

        return controllers

    def return_resource(self, p_file):
        return static_file(p_file, root='assets')

    def run_app(self):
        self.app.run(host=self.host, port=self.port, quiet=False, debug=True)

PoParser.compile_po_files()
app = LibreScanWeb()
app.run_app()
