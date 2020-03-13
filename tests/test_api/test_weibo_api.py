import unittest

from music_focus.api import weibo_api
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

    def test_parse_focus_by_title(self):
        print('test_parse_focus_by_title~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        r = weibo_api._parse_focus_by_title('#新裤子巡演#')
        print(r)

    def test_get_focuses_by_user(self):
        print('test_get_focuses_by_user~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        user = User(id=6724189443, name='新裤子乐队_',
                    gender=Gender.male, verified=True, description='', followers_cnt=0, follow_cnt=0,
                    profile=0, posts=1076036724189443, video=0, super_topic=0, album=0)
        r = weibo_api.get_focuses_by_user(user)
        print(r)

    def test_get_videos_by_user(self):
        print('test_get_videos_by_user~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        user = User(id=6724189443, name='新裤子乐队_',
                    gender=Gender.male, verified=True, description='', followers_cnt=0, follow_cnt=0,
                    profile=0, posts=1076036724189443, video=0, super_topic=0, album=0)
        videos = weibo_api.get_videos_by_user(user)
        print(videos)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
