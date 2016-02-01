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
from imgurpython import ImgurClient


class Client:
	""" Returns a client object to handle requests to imgur API """

	def __init__(self, static):
		config = static.get_bot_settings()
		self.client_id = config.get('credentials', 'client_id')
		self.client_secret = config.get('credentials', 'client_secret')
		self.refresh_token = config.get('credentials', 'refresh_token')

	def login(self):
	    client = ImgurClient(
	    	self.client_id, self.client_secret, None, self.refresh_token)
	    return client