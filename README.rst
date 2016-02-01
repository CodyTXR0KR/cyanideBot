cyanide_bot 
===========
An imgur.com user bot leveraging the `imgurpython API <https://github.com/Imgur/imgurpython>`_

:Developer:
	Cody Rocker
:License:
	GNU/GPLv2
:Date:
	2016

- **Requirements**
	+ Python 3
	+ `imgurpython <https://github.com/Imgur/imgurpython>`_

Install dependencies and clone source
-------------------------------------

This code is not meant for distribution so configuration is not user friendly, but if you `really` want to play with it,
continue reading...

.. code-block:: bash

	# if you dont have pip3 on your system
	$ sudo apt-get install python3-pip
	
	# install imgur python api for python 3
	$ pip3 install imgurpython

	# clone repository
	$ git clone https://github.com/CodyTXR0KR/cyanide_bot

Getting started
---------------

Visit `api.imgur.com <http://api.imgur.com/>`_ and `register a new application <https://api.imgur.com/oauth2/addclient>`_.
Make note of the Client_id and Client_secret.

Installation
^^^^^^^^^^^^

.. code-block:: bash
	
	# Navigate to the package directory
	$ cd path/to/cyanide_bot

	# Install the package locally
	$ python3 setup.py install

	# If you will be modifying the source use this instead
	$ python3 setup.py develop

cyanide-bot includes a shell script so you can run it from anywhere after installation

Run cyanide-bot
^^^^^^^^^^^^^^^

.. code-block:: bash
	
	# Run it without arguments first to configure the program
	$ cyanide_bot

	# once configuration is completed you can run
	$ cyanide_bot -h
	# or
	$ cyanide_bot --help
	# to look through the available command line options

All the functional `bot logic` is located in the ``cyanide_bot\cyanide_bot\bot_logic.py`` module.
If you will be modifying the code please respect Imgurs API rules and TOS, so you don;t ruin it for the rest of us.

--------------------

If you run into trouble feel free to email the developer_. 

.. _developer: mailto:cody.rocker.83@gmail.com