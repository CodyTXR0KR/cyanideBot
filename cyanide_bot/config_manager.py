# -*- coding: utf-8 -*-

### cyanide_bot
### GNU/GPL v2
### Author: Cody Rocker
### Author_email: cody.rocker.83@gmail.com
### 2016
#-----------------------------------
#   Requires:                    """
#    - Python 2.7                """
#    - imgurpython               """
#-----------------------------------
import os

APPLICATION_NAME = "CyanideBot"
CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config')
CONFIG_PATH = os.path.join(CONFIG_DIR, APPLICATION_NAME)


def get_config():
    ''' Create a config parser for reading INI files '''
    try:
        import ConfigParser
        return ConfigParser.ConfigParser()
    except:
        import configparser
        return configparser.ConfigParser()


def load_config(config_file):
    config = get_config()
    try:
        config.read(os.path.join(CONFIG_PATH, config_file))
        return config
    except:
        return config


def write_config(config_instance, config_file):
    try:  # try to write to directory, or
        with open(os.path.join(CONFIG_PATH, config_file), 'w') as configFile:
            config_instance.write(configFile)
    except:  # create the directory, if necessary
        os.mkdir(CONFIG_PATH)
        with open(os.path.join(CONFIG_PATH, config_file), 'w') as configFile:
            config_instance.write(configFile)