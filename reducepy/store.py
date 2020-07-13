#!/usr/bin/env python

from redis import (
    Redis,
    exceptions
)

from typing import Optional


class Store(object):
    """Class used to store shorten ids and urls."""

    def __init__(self, redis: Redis):
        self._redis = redis


    def keep(self, key: str, value: str):
        try:
            self._redis.set(key, value)
        except exceptions.ConnectionError:
            print('Redis connection error when trying to keep long url')


    def value_of(self, key: str) -> Optional[str]:
        try:
            url = self._redis.get(key)
            if url:
                return url.decode('utf-8')
            return None
        except exceptions.ConnectionError:
            print('Redis connection error when trying to get long url')
            return None
