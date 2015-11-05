import subprocess

from utils.task import Task


class Tesseract(Task):

    def __init__(self, p_config_params):
        self.language = p_config_params['lang']
        self.output_format = p_config_params['output-format']
        self.photo_extension = p_config_params['input-extension']

    def exec(self, params):
        working_path = params['input_dir'] + '/processed'
        input_path = params['input_dir'] + '/processed/' + params['photo'] + "." + self.photo_extension
        output_path = params['input_dir'] + '/processed/' + params['photo']
        command = "tesseract -l " + self.language + " " + input_path + " " + output_path + " " + self.output_format
        subprocess.call(command, shell=True)
