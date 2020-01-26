import unittest
from datetime import datetime

from music_focus.beans.post import Post
from music_focus.processors.compute_posts_hot_processor import ComputePostsHotProcessor


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        posts = {
            'rock': [
                Post(id=4464282798056885, user_id=1254762805, user_name='痛仰乐队',
                     time=datetime(2020, 1, 24, 0, 0), content='一方有难，八方支援。',
                     share_cnt=19353, comment_cnt=7713, like_cnt=116585, comments=[])
            ]
        }
        tmp_result = {'posts': posts}
        p = ComputePostsHotProcessor()
        p.run({}, tmp_result, {})
        print(tmp_result['scores'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
