#!/usr/bin/env python

import unittest
from reducepy.url_shorten import UrlShorten

class UrlShorterTest(unittest.TestCase):

    def test_md5(self):
        md5_text = UrlShorten.md5('https://www.google.com')
        self.assertEqual(md5_text, '8ffdefbdec956b595d257f0aaeefd623')
