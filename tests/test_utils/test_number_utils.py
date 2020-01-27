import unittest

from music_focus.utils.number_utils import parse_number


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        number_strs = ['123', '128万', '1.2亿']
        for number_str in number_strs:
            number = parse_number(number_str)
            print('{} -> {}'.format(number_str, number))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
