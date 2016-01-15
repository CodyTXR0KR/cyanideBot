#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import urllib2
import re
import smtplib

# Email dependancies
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from time import strftime

# Requires Imgur's Python api to be installed. >> https://github.com/Imgur/imgurpython
# Documentation >> https://api.imgur.com/
from imgurAPIClient import StartClient
from helpers import get_config

### GNU GENERAL PUBLIC LICENSE
### Author: cody.rocker.83@gmail.com
### 2016
#-----------------------------------
#   Requires:                    """
#    - Python 2.7                """
#    - imgurpython               """
#-----------------------------------

#  TODO -- Add logging

""" DEFINES """

#  Retrieve account credentials from config file
config = get_config()
config.read('auth.ini')
password = config.get('credentials', 'password')

#  Message handler settings (errors/confirmations sent to dev email)
botmail = config.get('credentials', 'botmail')
devmail = config.get('credentials', 'devmail')

#  Initialize imgurAPIClient
client = StartClient()


#  Email message to developer
def SendMessage(MODE, message):
    msg = MIMEMultipart()
    msg['From'] = botmail
    msg['To'] = devmail

    if MODE == "message":
        msg['Subject'] = 'webdev-server.cyanideBot -- message'
        text = MIMEText("cyanideBot.explosmdotnet posted an image to Imgur\n" + message)

    elif MODE == "error":
        msg['Subject'] = 'webdev-server.cyanideBot -- error'
        text = MIMEText("cyanideBot.explosmdotnet failed with error:\n" + message)

    msg.attach(text)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(botmail, password)
    server.sendmail(botmail, devmail, msg.as_string())
    server.quit()


#  Return formatted date string
def GetDate():
    return strftime('%b %d %Y')


#  Returns a url dictionary containing regEx matches
def GetUrls():
    urls = {}  # define in local scope to ensure clean empty dict
    try:
        response = urllib2.urlopen('http://explosm.net')
        html = response.read()
        urls['imgUrl'] = (
            "http://" + re.findall(r'<img id="featured-comic" src="//(.*?)"/></a>',
            html)[0])
        urls['permalinkUrl'] = (
            re.findall(r'<input id="permalink" type="text" value="(.*?)" onclick=',
            html)[0])
        urls['hotlinkUrl'] = (
            re.findall(r'<a href="(.*?)"><img id="featured-comic" src="',
            html)[0])
        return urls
    except Exception as error:
        SendMessage("error", error)
        sys.exit()


#  Scrape explosm.net for urls && upload w/ metadata
def MakePost(client):
    urls = GetUrls()
    meta = {}  # define in local scope to ensure clean empty dict
    meta['album'] = None
    meta['name'] = None
    meta['title'] = "Daily dose of Cyanide for " + GetDate()
    meta['description'] = (
        "Todays comic -- %s\nPermalink -- %s\nFind more at -- http://explosm.net" % (
            urls['hotlinkUrl'], urls['permalinkUrl']))
    try:
        response = client.upload_from_url(urls['imgUrl'], meta, anon=False)
        SendMessage("message", response['link'])
        sys.exit()
    except Exception as error:
        SendMessage("error", error)
        sys.exit()

""" PROGRAM FUNCTIONALITY """

if __name__ == '__main__':
    MakePost(client)