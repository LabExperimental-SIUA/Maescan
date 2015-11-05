import yaml

from utils.pdfBeads import PDFBeads
from utils.scantailor import Scantailor
from utils.tesseract import Tesseract


class TaskManager:

    def __init__(self, p_working_dir):
        self.working_dir = p_working_dir
        self.output_makers = [PDFBeads()]  # OutputMaker
        configuration = self.get_configuration()
        scantailor = Scantailor(configuration['scantailor'])
        tesseract = Tesseract(configuration['tesseract'])
        self.tasks = [scantailor, tesseract]

    def process(self, p_list):
        for photo in p_list:
            params = {'input_dir': self.working_dir, 'photo': photo}
            for task in self.tasks:
                task.exec(params)

    def generate(self):
        for output_maker in self.output_makers:
            output_maker.make(self.working_dir, "out")

    # Loads tools configuration from the project configuration.
    def get_configuration(self):
        config_path = self.working_dir + "/.projectConfig.yaml"
        f = open(config_path)
        data_map = yaml.safe_load(f)
        f.close()
        return data_map

'''
Example:
    t = TaskManager("/home/diugalde/Desktop")
    t.process(['015', '016'])
    t.generate()
'''