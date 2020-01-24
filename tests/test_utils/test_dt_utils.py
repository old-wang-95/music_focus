import unittest
from datetime import datetime

from music_focus.utils import dt_utils


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        print('test~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('now\t{}'.format(datetime.now()))
        time_strs = ['15分钟前', '10秒前', '1小时前', '01-21', '2018-11-30', '']
        for time_str in time_strs:
            print('{}\t{}'.format(time_str, dt_utils.parse_date_time(time_str)))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
