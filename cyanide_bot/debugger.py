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
from time import strftime


class Color:

    YELLOW = '\033[93m'
    LT_RED = '\033[91m'
    LT_BLUE = '\033[94m'
    LT_GREEN = '\033[92m'

    BOLD = '\033[1m'
    RESET = '\033[0m'


class Debug:
    """ Simple debug/logger  >>
    Set output options in config/user_prefs.ini
    """

    def __init__(self, app_name, debug=True, color_output=False):
        self.app_name = app_name
        self.DEBUG = debug
        self.color_output = color_output

        if self.color_output:
            self.log('%s%s debugger initialized...%s' % (
                Color.YELLOW, self.app_name, Color.RESET))
        else:
            self.log('%s debugger initialized...' % (self.app_name))

    def log(self, msg):
        if self.DEBUG:
            if self.color_output:
                print (('%s>>%s %sDEBUG%s <%s> -- %s' % (
                    Color.BOLD, Color.RESET, Color.YELLOW,
                    Color.RESET, self.time_stamp(), msg)))
            else:
                print (('>> DEBUG <%s> -- %s' % (self.time_stamp(), msg)))

    def log_error(self, msg, error):
        if self.color_output:
            print (('%s>>%s %sERROR%s <%s> -- %s%s%s' % (
                Color.BOLD, Color.RESET, Color.LT_RED, Color.RESET,
                self.time_stamp(), Color.YELLOW, msg, Color.RESET)))
            print (('\t\t\t\t-- Error: %s' % (str(error))))
        else:
            print (('>> ERROR <%s> -- %s' % (self.time_stamp(), msg)))
            print (('\t\t-- Error: %s' % (str(error))))

    def time_stamp(self):
        return strftime('%b %d %Y - %-I:%M%p')