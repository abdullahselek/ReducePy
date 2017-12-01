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
        response = self.app.get('/?url=https://www.google.com', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'http://localhost:5000/ZDYyMw', response.data)
