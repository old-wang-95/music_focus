import os
import pickle
import time
from hashlib import sha1


class Cache:

    def __init__(self, cache_dir='./tmp'):
        self._cache_dir = cache_dir

    def _get_cache_file_name(self, key):
        s = sha1()
        s.update(str(key).encode('utf-8'))
        return self._cache_dir + '/' + s.hexdigest()

    def _save_cache(self, key, value, timeout):
        result = {
            'result': value,
            'timeout': timeout,
            'timestamp': time.time()
        }
        with open(self._get_cache_file_name(key), 'wb') as f:
            pickle.dump(result, f)

    def _exist_cache(self, key):
        cache_file = self._get_cache_file_name(key)
        if not os.path.exists(cache_file):
            return False

        with open(cache_file, 'rb') as f:
            result = pickle.load(f)
        if time.time() - result['timestamp'] >= result['timeout']:
            os.remove(cache_file)
            return False

        return True

    def _get_cache(self, key):
        with open(self._get_cache_file_name(key), 'rb') as f:
            result = pickle.load(f)
        return result['result']

    def cache(self, key, func, *func_args, timeout=60 * 30, **func_kwargs):
        if self._exist_cache(key):
            return self._get_cache(key)
        value = func(*func_args, **func_kwargs)
        self._save_cache(key, value, timeout)
        return value
