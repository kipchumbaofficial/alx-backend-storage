#!/usr/bin/env python3
'''Cache class module:
    Stores data in redis
'''
import uuid
import redis
from typing import Union, Callable, Optional


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

    def get(self, key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        '''get method:
            Gets the original type of the value of a key
        '''
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_int(self, key: str) -> Optional[int]:
        '''get_int method:
            Retrieves an integer
        '''
        value = self.get(key, fn=int)
        if isinstance(value, int):
            return value
        return None

    def get_str(self, key: str) -> Optional[str]:
        '''get_str method:
            Retrieves a String from redis
        '''
        value = self.get(key, fn=lambda x: x.decode('utf-8'))
        if isinstance(value, str):
            return value
        return None
