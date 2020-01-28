import json
import unittest
from datetime import datetime

from music_focus.beans.post import Post
from music_focus.processors.transform_posts_result_processor import TransformPostsResultProcessor


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        workflow_input = {
            'posts': {
                'scores': {
                    'rock': [7000, 348680]},
                'posts': {
                    'rock': [
                        Post(id=1, user_id=1, user_name='痛仰乐队', time=datetime(2020, 1, 24, 0, 0), content='',
                             share_cnt=1, comment_cnt=1, like_cnt=1, link='', comments=[]),
                        Post(id=2, user_id=2, user_name='老王乐队', time=datetime(2020, 1, 25, 0, 0), content='',
                             share_cnt=2, comment_cnt=2, like_cnt=2, link='', comments=[])
                    ]
                }
            }
        }
        workflow_output = {}
        p = TransformPostsResultProcessor()
        p.run(workflow_input, {}, workflow_output)
        print(json.dumps(workflow_output['result'], ensure_ascii=False, indent=2))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
