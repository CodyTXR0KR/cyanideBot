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
from imgurpython import ImgurClient
from config_manager import load_config, write_config
from helpers import get_input

"""

    This script uses a config (*.ini) file to authorize a new
    imgur application/account pair and generate Oauth2 tokens.

    The client_ID and client_secret are generated when
    the app is registered with imgur developer API.

    Documentation >> https://api.imgur.com/
    Example config >> https://github.com/Imgur/imgurpython/blob/master/examples/auth.ini

"""

#  TODO -- Add functionality to auto-generate the config files (if not found)


def authenticate():
    # Get client ID and secret from auth.ini
    config = load_config('bot_settings.ini')
    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    client = ImgurClient(client_id, client_secret)

    # Authorization flow, pin example (see docs for other auth types)
    authorization_url = client.get_auth_url('pin')

    print (("\nGo to the following URL: {0}".format(authorization_url)))

    # Read in the pin, handle Python 2 or 3 here.
    pin = get_input("Enter pin code: ")

    # ... redirect user to `authorization_url`, obtain pin (or code or token) ...
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    config.set('credentials', 'refresh_token', credentials['refresh_token'])
    write_config(config, 'bot_settings.ini')

    print ("Authentication successful! Here are the details:")
    print (("   Access token:  {0}".format(credentials['access_token'])))
    print (("   Refresh token: {0}".format(credentials['refresh_token'])))

    return client