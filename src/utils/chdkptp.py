import subprocess
from subprocess import call


class Chdkptp:

    # chdk_path to CHDKPTP
    global chdk_path
    chdk_path = '/usr/bin/chdkptp'

    @staticmethod
    def string_maker(p_usb_bus, p_usb_id, p_extra):
        chdk_string = "%s  -e\"connect -b=%s -d=%s%s" \
            % (chdk_path, p_usb_bus, p_usb_id, p_extra)
        print(chdk_string)
        return chdk_string

    def connect_string(p_cam):
        bus_string = "(%s -elist | %s -n1| cut -f4 -d' '| sed -e 's/b\=//g')" \
            % (chdk_path, p_cam.pos)
        
        id_string = "(%s -elist | %s -n1| cut -f5 -d' '| sed -e 's/d\=//g')" \
            % (chdk_path, p_cam.pos)

        p_cam.usb_bus = subprocess.check_output(bus_string, shell=True).decode("utf-8")[:-1]
        p_cam.usb_id = subprocess.check_output(id_string, shell=True).decode("utf-8")[:-1]
        
        return p_cam
        
    @staticmethod
    def shoot(p_cam, p_save_path):
        extra = "\" -e\"remoteshoot " + p_save_path + " -tv=1/25\""
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)

    @staticmethod
    def prepare(p_cam, p_camera_config):
        p_cam = Chdkptp.connect_string(p_cam)
        extra = "\" -e'download orientation.txt /tmp'"
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)
        p_cam.orientation = subprocess.check_output("(cat /tmp/orientation.txt)", shell=True).decode(encoding='UTF-8')
        call("rm -rf /tmp/orientation.txt", shell=True)
        Chdkptp.set_zoom(p_cam, p_camera_config.zoom)
        Chdkptp.set_quality(p_cam)

    @staticmethod
    def rec_mode(p_cam):
        extra = "\" -erec"
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)

    @staticmethod
    def set_zoom(p_cam, p_zoom_level):
        extra = "\" -e'lua set_zoom("+p_zoom_level+")'"
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)

    @staticmethod
    def set_zoom(p_cam, p_zoom_level):
        extra = "\" -e'lua set_zoom("+str(p_zoom_level)+")'"
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)

    @staticmethod
    def set_quality(p_cam):
        extra = "\" -e'lua props=require(\"propcase\"); set_prop(props.QUALITY, 0); set_prop(props.RESOLUTION, 0);" \
                " set_nd_filter(2); set_config_value(291, 0);'"
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)
