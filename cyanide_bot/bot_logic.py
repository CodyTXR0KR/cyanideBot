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
import urllib.request
import urllib.error
import urllib.parse
import re
import smtplib
import keyring

# Email dependancies
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from time import strftime

from .imgur_api_client import Client


class ImgurBot():

    def __init__(self, static):
        self.static = static
        self.debug = static.debugger()
        self.load_settings()
        self.client = Client(static).login()
        self.debug.log('ImgurBot successfuly initialized.')

    def load_settings(self):
        self.debug.log('ImgurBot.load_settings()')
        config = self.static.get_bot_settings()
        self.botmail = config.get('messaging', 'botmail')
        self.devmail = config.get('messaging', 'devmail')
        self.messaging_enabled = config.getboolean('messaging', 'enabled')

    #  Email message to developer
    def send_message(self, MODE, message):
        self.debug.log('ImgurBot.send_message() :: sending %s...' % MODE)
        if self.messaging_enabled:
            msg = MIMEMultipart()
            msg['From'] = self.botmail
            msg['To'] = self.devmail

            if MODE == "message":
                msg['Subject'] = 'webdev-server.cyanideBot -- message'
                text = MIMEText(
                    'cyanideBot.explosmdotnet posted an image to Imgur\n'
                    '%s' % message)
            elif MODE == "error":
                msg['Subject'] = 'webdev-server.cyanideBot -- error'
                text = MIMEText(
                    'cyanideBot.explosmdotnet failed with error:\n'
                    '%s' % str(message))
            msg.attach(text)
            try:
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                server.ehlo()
                password = keyring.get_password('cyanide_bot', 'botmail')
                server.login(self.botmail, password)
                password = None
                server.sendmail(self.botmail, self.devmail, msg.as_string())
                server.quit()
            except Exception as error:
                self.debug.log_error('ImgurBot.send_message()', error)
                sys.exit()
            self.debug.log('ImgurBot.send_message() :: %s sent.' % MODE)
        else:
            self.debug.log('ImgurBot.send_message() :: messaging disabled.')

    ###==========================================================###
    ### -- CYANIDE-BOT functions                                 ###
    ### -- This is where specific behaviors should be modified.  ###
    ###==========================================================###

    def get_urls(self):
        self.debug.log('ImgurBot.get_urls()')
        urls = {}  # define in local scope to ensure clean empty dict

        try:
            response = urllib.request.urlopen('http://explosm.net')
            html = response.read()

            urls['imgUrl'] = 'http://{0}'.format(re.findall(
                b'<img id="featured-comic" src="//(.*?)"/></a>',
                    html)[0].decode('utf-8'))
            self.debug.log('Image Url: %s' % urls['imgUrl'])

            urls['permalinkUrl'] = re.findall(
                b'<input id="permalink" type="text" value="(.*?)" onclick=',
                    html)[0].decode('utf-8')
            self.debug.log('Permalink Url: %s' % urls['permalinkUrl'])

            urls['hotlinkUrl'] = re.findall(
                b'<a href="(.*?)"><img id="featured-comic" src="',
                    html)[0].decode('utf-8')
            self.debug.log('Hotlink Url: %s' % urls['hotlinkUrl'])
            return urls

        except Exception as error:
            self.send_message('error', error)
            self.debug.log_error('ImgurBot.get_urls()', error)
            sys.exit()

    def make_post(self, publish=False, tag_image=False, tag=''):
        self.debug.log('ImgurBot.make_post()')

        # Fetch image and build post metadata
        urls = self.get_urls()
        meta = {}
        meta['album'] = None
        meta['name'] = None
        meta['title'] = 'Daily dose of Cyanide for ' + get_date()
        meta['description'] = (
            'Permalink -- %s\nFind more at -- http://explosm.net' % (
                urls['permalinkUrl']))

        try:  # imgur_api functionality
            # Perform upload action from provided url
            upload_response = self.upload_from_url(urls['imgUrl'], meta)
            if publish:
                # Publish image to gallery if -p, --publish is true
                self.publish_to_gallery(
                    upload_response['item_id'], upload_response['title'])
            if tag_image:
                if tag is not '':
                    # Tag the image with user defined tag
                    self.tag_image(tag, upload_response['item_id'])

        except Exception as error:
            self.send_message('error', error)
            self.debug.log_error('ImgurBot.make_post() :: Failed.', error)
            sys.exit()

        self.send_message('message', upload_response['link'])
        self.debug.log('ImgurBot.make_post() :: Complete.')

    def upload_from_url(self, url, meta):
        self.debug.log('Uploading image...')
        try:
            upload_response = self.client.upload_from_url(url, meta, anon=False)
            response = {}
            response['item_id'] = upload_response['id']
            response['title'] = upload_response['title']
            response['link'] = upload_response['link']
        except Exception as error:
            self.debug.log_error('ImgurBot.upload_from_url()', error)
            sys.exit()
        self.debug.log('New image uploaded successfuly.')
        return response

    def publish_to_gallery(self, item_id, title):
        self.debug.log('Publishing image to gallery...')
        try:
            publish_response = self.client.share_on_imgur(item_id, title)
            self.debug.log('publish_response=%s' % publish_response)
        except Exception as error:
            self.debug.log_error('ImgurBot.publish_to_gallery()', error)
            sys.exit()
        self.debug.log('Image published to gallery.')

    def tag_image(self, tag, item_id):
        self.debug.log('Tagging imgage...')
        try:
            tag_response = self.client.gallery_tag_image(tag, item_id)
            self.debug.log('tag_response=%s' % tag_response)
        except Exception as error:
            self.debug.log_error('ImgurBot.tag_image()', error)
            sys.exit()
        self.debug.log('Image tagged with: [%s]' % tag)


#  Return formatted date string
def get_date():
    return strftime('%b %d %Y')