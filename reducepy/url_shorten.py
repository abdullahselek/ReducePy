#!/usr/bin/env python

import hashlib

class UrlShorten(object):
    """Class used to shorten given urls."""

    @staticmethod
    def md5(url):
        return hashlib.md5(url.encode('utf-8')).hexdigest()
