# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
import glob

class HocrService:
    def __init__(self):
        pass

    def get_path_file(self, id):
        path = '/home/labexp/LibreScanProjects/L15/processed/' #este va a ser el path de la imagen
        
        l = glob.glob(path + '*.hocr')
        l.sort()
        
        text_name = l[int(id)]
        return text_name

    def get_hocr_lines(self, file):
        os.system('hocr-lines '+file+' > /tmp/.libreScan_temp_file.txt')
        lines_file = open('.temp_file.txt','r')
        text = ""
        for line in lines_file:
            text = text+line
        lines_file.close()
        print(text)
        return {'text' : text}


    def save_hocr_text(self, file, text):

        new_words = text.split()
        new_words_len = len(new_words)
        tree = ET.ElementTree(file=file)
        ptr = 0
        for elem in tree.iter(tag='{http://www.w3.org/1999/xhtml}span'):
            if (elem.text == None):
                if(elem[0].tag == '{http://www.w3.org/1999/xhtml}strong'):
                    if(new_words_len > ptr):
                        elem[0].text = new_words[ptr]
                        ptr = ptr + 1
                    else:
                        elem[0].text = " "
            else:
                if(new_words_len > ptr):
                    elem.text = new_words[ptr]
                    ptr = ptr + 1
                else:
                    elem.text = " "

        tree.write(file)
