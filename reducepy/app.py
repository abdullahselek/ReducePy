#!/usr/bin/env python

from flask import (
    Flask,
    redirect
)
from flask import request
from redis import Redis
from reducepy.url_shorten import UrlShorten
from reducepy.store import Store

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
store = Store(redis)

def __create_shorten_url(url):
    unique, short_url = UrlShorten.shorten_url(url)
    store.keep(unique, url)
    return short_url

@app.route('/', methods=['POST'])
def shorten():
    if 'url' in request.form:
        url = request.form['url']
        return __create_shorten_url(url)
    else:
        return 'Please post a url', 400

@app.route('/<unique>')
def forward(unique):
    url = store.value_of(unique)
    if url:
        return redirect(url)
    else:
        return 'No url not found', 200    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
