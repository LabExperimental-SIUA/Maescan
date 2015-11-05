import os
import subprocess

from utils.outputMaker import OutputMaker


class PDFBeads(OutputMaker):

    def make(self, p_path, p_output_name):
        input_path = p_path + "/processed/"
        output_path = p_path + "/" + p_output_name
        command = "pdfbeads " + "*.tif > " + output_path + ".pdf"
        os.chdir(input_path)
        subprocess.call(command, shell=True)
