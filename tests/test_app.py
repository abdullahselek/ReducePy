#!/usr/bin/env python

import os
import tornado.web
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from reducepy import (
    ShortenUrlHandler,
    UniqueForwardHandler
)
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

class AppTest(AsyncHTTPTestCase):

    def setUp(self):
        super(AppTest, self).setUp()
        ## allow more time before timeout since we are doing remote access..
        os.environ["ASYNC_TEST_TIMEOUT"] = str(20)

    def get_app(self):
        return Application([(r'/', ShortenUrlHandler),
                            (r'/forward', UniqueForwardHandler)], debug=True, autoreload=False)

    def get_new_ioloop(self):
        return tornado.ioloop.IOLoop.instance()

    def test_shorten(self):
        post_data = {'url': 'https://www.google.com'}
        body = urlencode(post_data)
        response = self.fetch(r'/', method='POST', body=body)
        self.assertEqual(response.code, 200)
        # self.assertIn(b'{"shorten_url": "http://localhost:8888/ZDYyMw", "error": false}', response.body)

    def test_shorten_without_www(self):
        post_data = {'url': 'https://google.com'}
        body = urlencode(post_data)
        response = self.fetch(r'/', method='POST', body=body)
        self.assertEqual(response.code, 200)
        # self.assertIn(b'{"shorten_url": "http://localhost:8888/OTY5Zg", "error": false}', response.body)

    def test_shorten_with_path(self):
        post_data = {'url': 'http://www.cwi.nl:80/%7Eguido/Python.html'}
        body = urlencode(post_data)
        response = self.fetch(r'/', method='POST', body=body)
        self.assertEqual(response.code, 200)
        # self.assertIn(b'{"shorten_url": "http://localhost:8888/NTc3NA", "error": false}', response.body)

    def test_shorten_with_invalid_url(self):
        post_data = {'url': 'abdullahselek.com'}
        body = urlencode(post_data)
        response = self.fetch(r'/', method='POST', body=body)
        self.assertEqual(response.code, 400)
        # self.assertIn(b'{"message": "Please post a valid url", "error": true}', response.body)

    def test_shorten_empty(self):
        post_data = {'key': 'https://www.google.com'}
        body = urlencode(post_data)
        response = self.fetch(r'/', method='POST', body=body)
        self.assertEqual(response.code, 400)
        # self.assertIn(b'{"message": "Please post a url", "error": true}', response.body)

    def test_shorten_unsupported(self):
        post_data = {'key': 'https://www.google.com'}
        body = urlencode(post_data)
        response = self.fetch(r'/', method='PATCH', body=body)
        self.assertEqual(response.code, 405)

    def test_forward(self):
        response = self.fetch('/forward?unique=YjUwYQs', method='GET')
        self.assertEqual(response.code, 200)
        # self.assertIn(b'{"message": "No url not found with given unique", "error": true}', response.body)
