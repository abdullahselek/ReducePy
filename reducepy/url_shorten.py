#!/usr/bin/env python

import hashlib
import base64

try:
    # python 3
    from urllib.parse import urlunparse
except ImportError:
    from urlparse import urlunparse

class UrlShorten(object):
    """Class used to shorten given urls."""

    @staticmethod
    def md5(url):
        return hashlib.md5(url.encode('utf-8')).hexdigest()

    @staticmethod
    def byte_array(url):
        byte_array = bytearray()
        byte_array.extend(map(ord, url))
        return byte_array

    @staticmethod
    def get_last_x_element(byte_array, x):
        return byte_array[-x:]

    @staticmethod
    def string_from_bytes(byte_array):
        return "".join(map(chr, byte_array))

    @staticmethod
    def encode_base64(byte_array):
        return str(base64.b64encode(byte_array).decode('utf-8'))

    @staticmethod
    def create_unique(url):
        url_hash = UrlShorten.md5(url)
        url_byte_array = UrlShorten.byte_array(url_hash)
        last_four_bytes = UrlShorten.get_last_x_element(url_byte_array, 4)
        return UrlShorten.encode_base64(last_four_bytes)[:-2]

    @staticmethod
    def shorten_url(url, scheme, netloc):
        unique = UrlShorten.create_unique(url)
        return unique, urlunparse((scheme, netloc, unique, None, None, None))
