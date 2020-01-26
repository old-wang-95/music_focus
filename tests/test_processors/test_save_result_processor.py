import unittest
from datetime import datetime

from music_focus.beans.post import Post
from music_focus.processors.save_result_processor import SaveResultProcessor


class Test(unittest.TestCase):

    def setUp(self):
        self.data_dir = 'tests/data'

    def test_save_posts(self):
        print('test_save_posts~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        posts = {
            'rock': [
                Post(id=4464282798056885, user_id=1254762805, user_name='痛仰乐队',
                     time=datetime(2020, 1, 24, 0, 0), content='一方有难，八方支援。',
                     share_cnt=100, comment_cnt=200, like_cnt=5000, comments=[]),
                Post(id=1111111111111111, user_id=2222222222, user_name='老王乐队',
                     time=datetime(2020, 1, 25, 0, 0), content='没啥好说的',
                     share_cnt=19353, comment_cnt=7713, like_cnt=116585, comments=[])
            ]
        }
        scores = {
            'rock': [7000, 348680]
        }
        tmp_result = {'posts': posts, 'scores': scores}
        p = SaveResultProcessor(self.data_dir)
        p.run({}, tmp_result, {})

    def test_save_focuses(self):
        print('test_save_focuses~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        focuses = {
            'rock': ['老王乐队发新歌', '痛仰灾情捐款', '告五人全国巡演']
        }
        scores = {
            'rock': [500, 1000, 100]
        }
        tmp_result = {'focuses': focuses, 'scores': scores}
        p = SaveResultProcessor(self.data_dir)
        p.run({}, tmp_result, {})

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
