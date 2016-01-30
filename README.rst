cyanideBot 
==========
<http://imgur.com/user/explosmdotnet>

:Developer:
	Cody Rocker
:License:
	GNU/GPLv2
:Date:
	2016

- **Requirements**
	+ Python 2.7
	+ `imgurAPIClient <https://github.com/Imgur/imgurpython>`_

Install
-------

This code is not really meant for distribution so configuration is not user friendly, but if you `really` want to play with it,
continue reading...

.. code-block:: bash
	
	# install imgur python api
	$ pip install imgurpython

	# clone repository
	$ git clone https://github.com/CodyTXR0KR/cyanideBot

Getting started
---------------

Visit `api.imgur.com <http://api.imgur.com/>`_ and `register a new application <https://api.imgur.com/oauth2/addclient>`_.
Make note of the Client_id and Client_secret.

Configure your bot:

.. code-block:: bash
	
	# navigate to cyanide bot directory
	$ cd /path/to/cyanideBot

	# take ownership of the project
	$ sudo chown [user] cyanideBot

	# generate configuration directory
	# - cyanideBot/
	#     - .git/
	#     - .gitignore
	#     - LICENSE
	#     - README.rst
	#     - config/
	#         - auth.ini
	#     - cyanideBot/
	#         - auth.py
	#         - cyanideBot.py
	#         - helpers.py
	#         - imgurAPIClient.py
	#     - images/

	$ mkdir -p config
	$ touch config/auth.ini

	# edit config file
	$ nano config/auth.ini

	# make the config mirror the following:
	[credentials]
	client_id = your_client_id
	client_secret = your_client_secret
	refresh_token = 
	botmail = email_acct_for_bot # use gmail because it's free and easy
	devmail = your_email
	password = password_for_botmail_acct

	# authorize your bot with your imgur acct,
	# or create and sign into an acct specifically
	# for the bot before proceeding.
	$ python cyanideBot/auth.py

	# follow the prompts to generate your refresh token
	# you may want to backup your config at this point.

Run your bot:

.. code-block:: bash

	# if you're not already in the bot dir
	$ cd path/to/cyanideBot

	# from the top level of the project
	$ ./cyanideBot/cyanideBot.py

If you run into trouble feel free to email the developer_. 

.. _developer: mailto:cody.rocker.83@gmail.com