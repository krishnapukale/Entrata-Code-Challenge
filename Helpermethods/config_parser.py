import configparser
import os
from pathlib import Path


from Config import global_var

class ReadProp:

    @staticmethod
    def get_config_data(ini_file, key):
        config = configparser.ConfigParser()
        file_path = os.path.join(global_var.CONFIG_PATH, ini_file)
        read_success = config.read(file_path)
        if read_success:
            return config.get(key)
        else:
            print("Failed to read configuration file.")