#!/usr/bin/env python

"""URL shortener service is written with Python using Tornado and Redis"""

from __future__ import absolute_import

__author__ = "Abdullah Selek"
__email__ = "abdullahselek.os@gmail.com"
__copyright__ = "Copyright (c) 2017 Abdullah Selek"
__license__ = "MIT License"
__version__ = "1.2.0"
__url__ = "https://github.com/abdullahselek/ReducePy"
__download_url__ = "https://github.com/abdullahselek/ReducePy"
__description__ = "URL shortener service is written with Python using Tornado and Redis"

from .app import MainHandler
from .store import Store
from .url_shorten import UrlShorten
