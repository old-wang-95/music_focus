import unittest

from music_focus.processors.gen_focus_processor import GenFocusProcessor


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        p = GenFocusProcessor()
        tmp_result = {}
        p.run({}, tmp_result, {})
        print(tmp_result['focuses'])
        print(tmp_result['scores'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
