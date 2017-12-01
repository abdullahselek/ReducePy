#!/usr/bin/env python

from flask import Flask
from flask import request
from redis import Redis
from reducepy.url_shorten import UrlShorten

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
def shorten():
    if request.method == 'POST':
        if 'url' in request.form:
            url = request.form['url']
            return UrlShorten.shorten_url(url)
        else:
            return 'Please post a url', 403
    elif request.method == 'GET':
        url = request.args.get('url', '')
        return UrlShorten.shorten_url(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
