# -*- coding: utf-8 -*-
from helpers import get_config
from imgurpython import ImgurClient

""" Returns a client object to handle requests to imgur API """

#  TODO -- Check to make sure the refresh_token exists
#  TODO -- Handle failed authentication for lost/corrupt config


def StartClient():
    # Get credentials from auth.ini
    config = get_config()
    config.read('auth.ini')  # this is the file that holds user credentials
    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')
    refresh_token = config.get('credentials', 'refresh_token')

    # Start client
    client = ImgurClient(client_id, client_secret, None, refresh_token)
    return client