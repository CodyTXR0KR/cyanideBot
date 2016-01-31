# -*- coding: utf-8 -*-
from config_manager import load_config
from imgurpython import ImgurClient

""" Returns a client object to handle requests to imgur API """

#  TODO -- Check to make sure the refresh_token exists
#  TODO -- Handle failed authentication for lost/corrupt config

class Client:

	def __init__(self):
		config = load_config('imgur_api_keys.ini')
		self.client_id = config.get('credentials', 'client_id')
		self.client_secret = config.get('credentials', 'client_secret')
		self.refresh_token = config.get('credentials', 'refresh_token')

	def start(self):
	    client = ImgurClient(
	    	self.client_id, self.client_secret, None, self.refresh_token)
	    return client