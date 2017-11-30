#!/usr/bin/env python

import hashlib

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
