#!/usr/bin/env python

import unittest
from reducepy import app

class AppTest(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
 
    # executed after each test
    def tearDown(self):
        pass

    def test_shorten(self):
        response = self.app.post(
            '/',
            data=dict(url='https://www.google.com'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'http://localhost:5000/ZDYyMw', response.data)

    def test_shorten_without_www(self):
        response = self.app.post(
            '/',
            data=dict(url='https://google.com'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'http://localhost:5000/OTY5Zg', response.data)

    def test_shorten_with_path(self):
        response = self.app.post(
            '/',
            data=dict(url='http://www.cwi.nl:80/%7Eguido/Python.html'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'http://localhost:5000/NTc3NA', response.data)

    def test_shorten_with_invalid_url(self):
        response = self.app.post(
            '/',
            data=dict(url='abdullahselek.com'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Please post a valid url', response.data)

    def test_shorten_empty(self):
        response = self.app.post(
            '/',
            data=dict(key='https://www.google.com'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Please post a url', response.data)

    def test_shorten_unsupported(self):
        response = self.app.patch(
            '/',
            data=dict(url='https://www.google.com'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 405)

    def test_forward(self):
        response = self.app.get('/YjUwYQ', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No url not found', response.data)
