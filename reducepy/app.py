#!/usr/bin/env python

import os
import tornado.ioloop
import tornado.web
import json

from redis import Redis
from reducepy.url_shorten import UrlShorten
from reducepy.store import Store

from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

from urllib.parse import urlparse


redis = Redis(host='redis', port=6379)
store = Store(redis)

try:
    scheme = os.environ['SCHEME']
    ip_address = os.environ['IP_ADDRESS']
    port = os.environ['PORT']
except KeyError:
    scheme = 'http'
    ip_address = 'localhost'
    port = 80

class MainHandler(tornado.web.RequestHandler):

    executor = ThreadPoolExecutor(max_workers=5)

    def __uri_validator(self, url: str):
        try:
            result = urlparse(url)
            if result.path:
                return all([result.scheme, result.netloc, result.path])
            return all([result.scheme, result.netloc])
        except:
            return False


    def __create_shorten_url(self, url: str):
        netloc = ip_address + ':' + str(port)
        unique, short_url = UrlShorten.shorten_url(url, scheme, netloc)
        store.keep(unique, url)
        return short_url


    @run_on_executor
    def background_task(self, url: str):
        if url:
            if self.__uri_validator(url):
                response = {
                    'error': False,
                    'shortened_url': self.__create_shorten_url(url)
                }
                return 201, json.dumps(response, sort_keys=True)
            response = {
                'error': True,
                'message': 'Please post a valid url'
            }
            return 400, json.dumps(response, sort_keys=True)
        else:
            response = {
                'error': True, 
                'message': 'Please post a url'
            }
        return 400, json.dumps(response, sort_keys=True)


    @tornado.gen.coroutine
    def post(self):
        url = self.get_argument('url', None)
        status_code, result = yield self.background_task(url)
        self.set_status(status_code)
        self.write(result)


    def get(self, *args):
        if len(args) == 1:                
            unique = args[0]
            url = store.value_of(unique)
            if url:
                return self.redirect(url)
            else:
                response = {
                    'error': True, 
                    'message': 'No url found with given unique'
                }
                self.set_status(404)
                return self.write(json.dumps(response, sort_keys=True))
        else:
            response = {
                'error': True, 
                'message': 'Please set only one argument path'
            }
            self.set_status(400)
            return self.write(json.dumps(response, sort_keys=True))


def main():
    app = tornado.web.Application(
        [(r'/', MainHandler),
         (r'/(.*)', MainHandler)],
        debug=False,
        )
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
