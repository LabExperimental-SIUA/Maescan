from threading import Thread
import time
import os

from PIL import Image
import yaml
import base64

from models.camera import Camera
from models.cameraConfig import CameraConfig
from patterns.singleton import Singleton
from utils.chdkptp import Chdkptp


class CameraService(metaclass=Singleton):

    pic_number = 0

    def __init__(self, p_working_dir=None):
        self.cams = [Camera("head"), Camera("tail")]
        self.working_dir = p_working_dir
        self.camera_config = None

    def set_save_path(self, p_working_dir):
        self.working_dir = p_working_dir + "/raw/"

    def set_camera_config(self):
        self.camera_config = self.get_configuration()

    def get_configuration(self):
        config_path = self.working_dir + "/.projectConfig.yaml"
        f = open(config_path)
        data_map = yaml.safe_load(f)["camera"]
        f.close()
        return CameraConfig(data_map["zoom"], data_map["iso"])

    def take_pictures(self):
        jobs = []
        pic_names = []
        save_path = self.working_dir + '/raw/'
        for cam in self.cams:
            CameraService.pic_number += 1
            pic_name = "lsp"+str(CameraService.pic_number).zfill(5)
            pic_names.append(pic_name)
            process = Thread(target=Chdkptp.shoot, args=(cam, save_path + pic_name))
            jobs.append(process)
            process.start()
            time.sleep(0.0005)

        for j in jobs:
            j.join()

        self.rotate(pic_names[0], pic_names[1])
        return pic_names

    def prepare_cams(self):
        for cam in self.cams:
            Chdkptp.prepare(cam, self.camera_config)
        for cam in self.cams:
            Chdkptp.rec_mode(cam)
        if self.cams[0].orientation == "left":
            self.cams.reverse()

    def rotate(self, p_left_photo, p_right_photo):
        save_path = self.working_dir + '/raw/'
        left_photo = Image.open(save_path + p_left_photo+".jpg")
        right_photo = Image.open(save_path + p_right_photo+".jpg")
        left_photo = left_photo.rotate(90)
        right_photo = right_photo.rotate(270)
        left_photo.save(save_path + p_left_photo+".jpg")
        right_photo.save(save_path + p_right_photo+".jpg")
        left_photo.close()
        right_photo.close()

    def delete_photos(self, p_photo_list):
        for photo in p_photo_list:
            os.remove(self.working_dir + "/raw/" + photo + ".jpg")

    def encode_image(self, p_img_name):
        with open(self.working_dir + '/raw/' + p_img_name + '.jpg', "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return encoded_string.decode(encoding="UTF-8")  # convert it to string
