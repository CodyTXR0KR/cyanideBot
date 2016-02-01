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
from .helpers import get_input


# This only needs to run to set-up the bot,
# or generate new tokens if they are lost.
def authenticate(settings):
    client_id = settings.get('credentials', 'client_id')
    client_secret = settings.get('credentials', 'client_secret')

    client = ImgurClient(client_id, client_secret)
    authorization_url = client.get_auth_url('pin')

    print(("\nGo to the following URL: {0}".format(authorization_url)))
    pin = get_input("Enter pin code: ")

    # ... redirect user to `authorization_url`,
    # obtain pin (or code or token) ...
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(
        credentials['access_token'], credentials['refresh_token'])

    settings.set('credentials', 'refresh_token', credentials['refresh_token'])

    print(("Authentication successful! Here are the details:"))
    print(("   Access token:  {0}".format(credentials['access_token'])))
    print(("   Refresh token: {0}".format(credentials['refresh_token'])))

    return client