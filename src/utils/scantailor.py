import subprocess

from utils.task import Task


class Scantailor(Task):
    def __init__(self, p_config_params, p_photo_extension="jpg"):
        self.config_params = p_config_params
        self.photo_extension = p_photo_extension
        self.base_command = self.generate_base_command()

    def generate_base_command(self):
        command = "scantailor-cli"
        for param in self.config_params:
            command += " -" + param + "=" + str(self.config_params[param])
        return command

    # Generates the command to be executed, concatenating the photo and input-output paths.
    def generate_final_command(self, p_project_path, p_photo):
        command = self.base_command
        input_path = p_project_path + "/raw/" + p_photo + "." + self.photo_extension
        output_path = p_project_path + "/processed/"
        command += " " + input_path + " " + output_path
        return command

    def exec(self, params):
        command = self.generate_final_command(params['input_dir'], params['photo'])
        subprocess.call(command, shell=True)
