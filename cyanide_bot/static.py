# -*- coding: utf-8 -*-

### cyanide_bot
### GNU/GPL v2
### Author: Cody Rocker
### Author_email: cody.rocker.83@gmail.com
### 2016
#-----------------------------------
#   Requires:                    """
#    - Python 3                  """
#    - imgurpython               """
#-----------------------------------
import os

from .config_manager import ConfigManager
from .bot_settings import first_run
from .debugger import Debug

APPLICATION_NAME = "cyanide-bot"
CONFIG_FILES = {'bot_settings': 'bot_settings.ini'}
CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config')


class StaticInterface:
    ## This class should only be initialized once
    """ accessor interface for static retrieval """

    def __init__(self):
        self.config_manager = ConfigManager(APPLICATION_NAME, CONFIG_DIR)
        """ ensure configuration files exist & initialize debug/logger"""
        # Initialize instance of bot_settings configParser
        self.bot_settings = self.config_manager.load_config(
            self.config_file('bot_settings'))
        if not self.bot_settings.sections():
            self.bot_settings.add_section('debugger')
            self.bot_settings.set('debugger', 'debug', 'True')
            self.bot_settings.set('debugger', 'color_coutput', 'False')
            self.save_settings()
            print('StaticInterface.__init__() >> first_run()')
            first_run(self)

        self.debug = Debug(APPLICATION_NAME,
            self.bot_settings.getboolean('debugger', 'debug'),
            self.bot_settings.getboolean('debugger', 'color_coutput'))

    def config_file(self, key):
        """ returns the fileName associated with key """
        return CONFIG_FILES[key]

    def get_bot_settings(self):
        """ returns a configParser instance of bot_settings """
        return self.bot_settings

    def save_settings(self):
        """ Save changes to configParser instance """
        self.config_manager.write_config(
            self.bot_settings, self.config_file('bot_settings'))

    # the Debug class is parented to StaticInterface to limit
    # initialization to a single instance
    def debugger(self):
        """ returns an instance of the Debug class for logging """
        return self.debug