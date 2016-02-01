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
import keyring

from .helpers import get_input
from .auth import authenticate
# Handle initialization of bot_settings.ini here


def first_run(static):
    debug = static.debugger()
    print(('\n** Take a moment to configure CyanideBot **'))
    print(('\nYou can reconfigure at any time by passing the argument '
           '--config\nor manually editing the config files '
           '(~/.config/CyanideBot)'))

    settings = static.get_bot_settings()

    set_messaging(settings)
    static.save_settings()

    register_application(settings)
    static.save_settings()

    authenticate(settings)
    static.save_settings()

    debug.log('Settings saved to ~/.config/CyanideBot/bot_settings.ini')


def set_messaging(settings):
    while True:    # infinite loop
        messaging = get_input('\nWould you like to enable messaging via '
            'email?\nThis is useful for automation.  yes/no: ')
        if messaging.lower() in ("yes", "y"):
            try:
                botmail = get_input('Email address the bot will be using to '
                    'send messages\n(example@email.com): ')
                password = get_input('Password for bot email acct: ')
                devmail = get_input('Email you would like to recieve messages '
                    'at\n(example@email.com): ')
            except KeyboardInterrupt:
                sys.exit()

            keyring.set_password('cyanide_bot', 'botmail', password)

            settings.add_section('messaging')
            settings.set('messaging', 'enabled', 'True')
            settings.set('messaging', 'botmail', botmail)
            settings.set('messaging', 'devmail', devmail)
            break
        elif messaging.lower in ("no", "n"):
            settings.add_section('messaging')
            settings.set('messaging', 'enabled', 'False')
            settings.set('messaging', 'botmail', '')
            settings.set('messaging', 'devmail', '')
            break
        else:
            print('Invalid entry. Enter yes or no')


def register_application(settings):
    print('\nVisit <https://api.imgur.com/oauth2/addclient> to register bot '
          'with\nimgur API. Make note of the client_id and client_secret you '
          'are assigned')
    try:
        client_id = get_input('Client ID: ')
        client_secret = get_input('Client Secret: ')
    except KeyboardInterrupt:
        sys.exit()

    settings.add_section('credentials')
    settings.set('credentials', 'client_id', client_id)
    settings.set('credentials', 'client_secret', client_secret)