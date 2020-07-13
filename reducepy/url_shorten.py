#!/usr/bin/env python

import hashlib
import base64

from urllib.parse import urlunparse
from typing import List, Tuple


class UrlShorten(object):
    """Class used to shorten given urls."""

    @staticmethod
    def md5(url: str):
        return hashlib.md5(url.encode('utf-8')).hexdigest()


    @staticmethod
    def byte_array(url: str) -> bytearray:
        byte_array = bytearray()
        byte_array.extend(map(ord, url))
        return byte_array


    @staticmethod
    def get_last_x_element(byte_array: List, x: int) -> bytes:
        return byte_array[-x:]


    @staticmethod
    def string_from_bytes(byte_array: List) -> str:
        return "".join(map(chr, byte_array))


    @staticmethod
    def encode_base64(byte_array: List) -> str:
        return str(base64.b64encode(byte_array).decode('utf-8'))


    @staticmethod
    def create_unique(url: str) -> str:
        url_hash = UrlShorten.md5(url)
        url_byte_array = UrlShorten.byte_array(url_hash)
        last_four_bytes = UrlShorten.get_last_x_element(url_byte_array, 4)
        return UrlShorten.encode_base64(last_four_bytes)[:-2]


    @staticmethod
    def shorten_url(url: str, scheme: str, netloc: str) -> Tuple[str, str]:
        unique = UrlShorten.create_unique(url)
        return unique, urlunparse((scheme, netloc, unique, None, None, None))
