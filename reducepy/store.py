#!/usr/bin/env python

from redis import Redis

class Store(object):
    """Class used to store shorten ids and urls."""

    def __init__(self, redis):
        self._redis = redis

    def keep(self, key, value):
        self._redis.set(key, value)

    def value_of(self, key):
        return self._redis.get(key)
