#!/usr/bin/env python

import os
import tornado.web
import json

from redis import Redis
from reducepy.url_shorten import UrlShorten
from reducepy.store import Store

try:
    # python 3
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

redis = Redis(host='redis', port=6379)
store = Store(redis)

try:
    scheme = os.environ['SCHEME']
    ip_address = os.environ['IP_ADDRESS']
    port = os.environ['PORT']
except KeyError:
    scheme = 'http'
    ip_address = 'localhost'
    port = 8888

class ShortenUrlHandler(tornado.web.RequestHandler):
    def __uri_validator(self, url):
        try:
            result = urlparse(url)
            if result.path:
                return all([result.scheme, result.netloc, result.path])
            return all([result.scheme, result.netloc])
        except:
            return False

    def __create_shorten_url(self, url):
        netloc = ip_address + ':' + str(port)
        unique, short_url = UrlShorten.shorten_url(url, scheme, netloc)
        store.keep(unique, url)
        return short_url

    def post(self):
        url = self.get_argument('url', None)
        if url:
            if self.__uri_validator(url):
                response = {
                    'error': False,
                    'shorten_url': self.__create_shorten_url(url)
                }
                return self.write(json.dumps(response, sort_keys=True))
            self.set_status(400)
            response = {
                'error': True,
                'message': 'Please post a valid url'
            }
        else:
            self.set_status(400)
            response = {
                'error': True, 
                'message': 'Please post a url'
            }
        return self.write(json.dumps(response, sort_keys=True))

class UniqueForwardHandler(tornado.web.RequestHandler):
    def get(self):
        unique = self.get_argument('unique', None)
        url = store.value_of(unique)
        if url:
            return self.redirect(url)
        else:
            response = {
                'error': True, 
                'message': 'No url found with given unique'
            }
            return self.write(json.dumps(response, sort_keys=True))

def main():
    app = tornado.web.Application(
        [
            (r'/', ShortenUrlHandler),
            (r'/forward', UniqueForwardHandler)
            ],
        debug=False,
        )
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
