# -*- coding: utf-8 -*-

from imgurpython import ImgurClient
from helpers import get_input, get_config

"""

    This script uses a config (*.ini) file to authorize a new
    imgur application/account pair and generate Oauth2 tokens.

    The client_ID and client_secret are generated when
    the app is registered with imgur developer API.

    Documentation >> https://api.imgur.com/
    Example config >> https://github.com/Imgur/imgurpython/blob/master/examples/auth.ini

    *** THIS MUST BE RUN SUCCESSFULY BEFORE USING MAIN APP ***

"""

#  TODO -- Add functionality to auto-generate the config files (if not found)


def authenticate():
    # Get client ID and secret from auth.ini
    config = get_config()
    config.read('auth.ini')
    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    client = ImgurClient(client_id, client_secret)

    # Authorization flow, pin example (see docs for other auth types)
    authorization_url = client.get_auth_url('pin')

    print (("Go to the following URL: {0}".format(authorization_url)))

    # Read in the pin, handle Python 2 or 3 here.
    pin = get_input("Enter pin code: ")

    # ... redirect user to `authorization_url`, obtain pin (or code or token) ...
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    config.set('credentials', 'refresh_token', credentials['refresh_token'])
    with open('auth.ini', 'w') as configfile:    # save
        config.write(configfile)

    print ("Authentication successful! Here are the details:")
    print (("   Access token:  {0}".format(credentials['access_token'])))
    print (("   Refresh token: {0}".format(credentials['refresh_token'])))

    return client

if __name__ == "__main__":
    authenticate()