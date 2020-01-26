import unittest
from music_focus.processors.fetch_posts_processor import FetchPostsProcessor


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        p = FetchPostsProcessor()
        tmp_result = {}
        p.run({}, tmp_result, {})
        print(tmp_result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
