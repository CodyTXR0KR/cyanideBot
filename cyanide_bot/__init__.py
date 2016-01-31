#!/usr/bin/python
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
import sys
import keyring

from bot_logic import run
from auth import authenticate
from config_manager import load_config, write_config
from helpers import get_input


def first_run():
	print('\n** Take a moment to configure CyanideBot **')
	print('\nYou can reconfigure at any time by passing the argument --reconfigure\n' \
		'or manually editing the config files (~/.config/CyanideBot)')
	enable_messaging()
	register_application()
	authenticate()
	run()
	
## this is a mess
## try while loops for validating input 
def enable_messaging():
	config = load_config('bot_settings.ini')
	try:
		messaging = get_input('\nWould you like to enable messaging via email?\n' \
			'This is useful for automation.  yes/no: ').strip()
	except KeyboardInterrupt:
		sys.exit()
	try:
		if messaging.lower() == 'yes' or messaging.lower() == 'y':
			try:
				botmail = get_input('Email address the bot will be using to send messages\n' \
					'(example@email.com): ').strip()
				password = get_input('Password for bot email acct: ').strip()
				devmail = get_input('Email you would like to recieve messages at\n' \
					'(example@email.com): ').strip()
			except KeyboardInterrupt:
				sys.exit()
			keyring.set_password('cyanide_bot', 'botmail', password)
			config.add_section('messaging')
			config.set('messaging', 'enabled', 'True')
			config.set('messaging', 'botmail', botmail)
			config.set('messaging', 'devmail', devmail)
			write_config(config, 'bot_settings.ini')
			print ('\n>> Settings saved to ~/.config/CyanideBot/bot_settings.ini')
			config = None

		elif messaging.lower() == 'no' or messaging.lower() == 'n':
			config.add_section('messaging')
			config.set('messaging', 'enabled', 'False')
			config.set('messaging', 'botmail', '')
			config.set('messaging', 'devmail', '')
			write_config(config, 'bot_settings.ini')
			print ('\n>> Settings saved to ~/.config/CyanideBot/bot_settings.ini')
			config = None

		else:
			print('Invalid entry. Enter yes or no')
			config = None
			enable_messaging()
	except KeyboardInterrupt:
		sys.exit()


def register_application():
	print('\nVisit <https://api.imgur.com/oauth2/addclient> to register bot with\n' \
		'imgur API. Make note of the client_id and client_secret you are assigned')
	try:
		client_id = get_input('Client ID: ').strip()
		client_secret = get_input('Client Secret: ').strip()
	except KeyboardInterrupt:
		sys.exit()

	config = load_config('bot_settings.ini')
	config.add_section('credentials')
	config.set('credentials', 'client_id', client_id)
	config.set('credentials', 'client_secret', client_secret)
	write_config(config, 'bot_settings.ini')
	print ('\n>> Settings saved to ~/.config/CyanideBot/bot_settings.ini')
	config = None


def main():
	config = load_config('bot_settings.ini')
	if not config.sections():
		first_run()
	else:
		run()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()