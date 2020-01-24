import unittest

from music_focus import weibo_api


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_user_info(self):
        print('test_get_user_info~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        user = weibo_api.get_user_info('1613258127')
        print(user)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
