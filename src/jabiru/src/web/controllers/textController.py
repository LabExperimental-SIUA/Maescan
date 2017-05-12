# -*- coding: utf-8 -*-
from bottle import request
from services.hocrService import HocrService

class TextController:
    def __init__(self, hocr_service):
        self.hocr_service = hocr_service

    def get_text(self, id):
        text_name = self.hocr_service.get_path_file(id)
        print(text_name)
        return self.hocr_service.get_hocr_lines(text_name)


    def save_text(self, id):
        data = request.json
        print(data)
        path = self.hocr_service.get_path_file(id)
        status = self.hocr_service.save_hocr_text(path, data['text'])

        return {'status' : 'status'}
