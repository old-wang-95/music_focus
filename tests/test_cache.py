import time
import unittest

from music_focus.cache import Cache


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_cache(self):
        print('test_cache~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        def func(word):
            print('run')
            return 'Hello, {}'.format(word)

        print('1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        r = Cache().cache('test', func, timeout=10, word='world')
        print(r)
        print('2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        r = Cache().cache('test', func, timeout=10, word='world')
        print(r)
        print('3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        time.sleep(10)
        r = Cache().cache('test', func, timeout=10, word='world')
        print(r)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
