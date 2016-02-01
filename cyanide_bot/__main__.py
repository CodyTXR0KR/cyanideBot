#!/usr/bin/env python3
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
import sys

from .static import StaticInterface
from .bot_logic import ImgurBot

_static = StaticInterface()

def main():
	cyanide_bot = ImgurBot(_static)

if __name__ == '__main__':
	try:
		main()
		_static.debug.log('cyanide-bot executed successfully.\n')
	except KeyboardInterrupt:
		sys.exit()