#!/usr/bin/env python3

import urllib.request
import urllib.error
import urllib.parse
import re

def isAnimation(html):
    try:
        current_comic = re.findall(
            b'<a href="(.*?)"><img id="featured-comic" src="//files.explosm.net/comics/.*"/></a>', 
                html)[0].decode('utf-8')
    except:
        pass
    if '//explosm.net/show/episode/' in current_comic:
        return True
    else:
        return False