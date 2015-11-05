
import os
from shutil import copyfile
import yaml

USERHOME = os.environ["HOME"]
RESOURCESPATH = './configuration'
LIBRESCANPATH = USERHOME + "/LibreScanProjects"
LSCONFIGPATH = USERHOME + "/.librescan"


def create_folders():
    os.mkdir(LIBRESCANPATH)
    os.mkdir(LSCONFIGPATH)


def create_config_files():
    template_path = "/defaultProjectConfig.yaml"
    project_template = RESOURCESPATH + template_path
    copyfile(project_template, LSCONFIGPATH + template_path)
    os.mknod(LSCONFIGPATH+"/projects.yaml")
    os.mknod(LSCONFIGPATH+"/config.yaml")

    data_map = {
        'email-receiver': 'librescan@gmail.com',
        'project': {
            'last-id': 0,
            'path': LIBRESCANPATH
        }
    }

    f = open(LSCONFIGPATH+"/config.yaml", 'w')
    f.write(yaml.dump(data_map, default_flow_style=False, allow_unicode=True))
    f.close()

create_folders()
create_config_files()
