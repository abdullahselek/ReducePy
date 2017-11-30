#!/usr/bin/env python

from flask import Flask
from flask import request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
def shorten():
    error = None
    if request.method == 'POST':
        if 'url' in request.form:
            url = request.form['url']
            return 'URL : %s' % url
        else:
            error = 'Please post a url'
    elif request.method == 'GET':
        url = request.args.get('url', '')
        return 'URL : %s' % url
    else:
        return 'Not supported method'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
