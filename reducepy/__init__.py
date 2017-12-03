#!/usr/bin/env python

"""URL shortener service is written with Python using Flask"""

from __future__ import absolute_import

__author__       = 'Abdullah Selek'
__email__        = 'abdullahselek@gmail.com'
__copyright__    = 'Copyright (c) 2017 Abdullah Selek'
__license__      = 'MIT License'
__version__      = '0.1'
__url__          = 'https://github.com/abdullahselek/ReducePy'
__download_url__ = 'https://github.com/abdullahselek/ReducePy'
__description__  = 'URL shortener service is written with Python using Flask'

from .app import app
from .url_shorten import UrlShorten
from .store import Store
