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
from config_manager import load_config
from imgurpython import ImgurClient


class Client:
	""" Returns a client object to handle requests to imgur API """

	def __init__(self):
		config = load_config('imgur_api_keys.ini')
		self.client_id = config.get('credentials', 'client_id')
		self.client_secret = config.get('credentials', 'client_secret')
		self.refresh_token = config.get('credentials', 'refresh_token')

	def start(self):
	    client = ImgurClient(
	    	self.client_id, self.client_secret, None, self.refresh_token)
	    return client