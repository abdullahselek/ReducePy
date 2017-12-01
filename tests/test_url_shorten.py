#!/usr/bin/env python

import unittest
from reducepy.url_shorten import UrlShorten

class UrlShorterTest(unittest.TestCase):

    def test_md5(self):
        md5_text = UrlShorten.md5('https://www.google.com')
        self.assertEqual(md5_text, '8ffdefbdec956b595d257f0aaeefd623')

    def test_byte_array(self):
        byte_array = UrlShorten.byte_array('https://www.google.com')
        self.assertIsNotNone(byte_array)

    def test_get_last_x_element(self):
        byte_array = UrlShorten.byte_array('https://www.google.com')
        last_four_element = UrlShorten.get_last_x_element(byte_array, 4)
        self.assertEqual(len(last_four_element), 4)

    def test_string_from_bytes(self):
        bytes = [112, 52, 52]
        string = UrlShorten.string_from_bytes(bytes)
        self.assertEqual(string, 'p44')

    def test_encode_base64(self):
        base64_encoded = UrlShorten.encode_base64('axcv4')
        self.assertEqual(base64_encoded, 'YXhjdjQ=')

    def test_shorten_url(self):
        short_url = UrlShorten.shorten_url('https://www.google.com')
        self.assertEqual(short_url, 'http://localhost:5000/ZDYyMw')
