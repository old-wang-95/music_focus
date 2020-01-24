import unittest

from music_focus import weibo_api
from music_focus.beans.user import User, Gender


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_user_info(self):
        print('test_get_user_info~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        user = weibo_api.get_user_info(1613258127)
        print(user)

    def test_get_posts_by_user(self):
        print('test_get_posts_by_user~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        user = User(id=1613258127, name='宋冬野',
                    gender=Gender.male, verified=True, description='', followers_cnt=0, follow_cnt=0,
                    profile=0, posts=1076031613258127, video=0, super_topic=0, album=0)
        posts = weibo_api.get_posts_by_user(user)
        print(posts)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
