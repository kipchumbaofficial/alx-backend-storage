#!/usr/bin/env python3
'''Cache class module:
    Stores data in redis
'''
import uuid
import redis
from typing import Union


class Cache:
    '''Cache Class:
        Creates a redis instance and stores data
    '''
    def __init__(self):
        '''Initializes the redis instance'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store method:
            Stores data in redis and returns the key
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
