import json
import unittest

from music_focus.beans.focus import Focus
from music_focus.processors.transform_focuses_result_processor import TransformFocusesResultProcessor


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        workflow_input = {
            'focuses': {
                'scores': {
                    'rock': [100, 200]},
                'focuses': {
                    'rock': [
                        Focus(title='#老王乐队#', description='', recent_read=100, read_cnt=1, discuss_cnt=1, member_cnt=1,
                              link=''),
                        Focus(title='#新裤子乐队#', description='', recent_read=200, read_cnt=2, discuss_cnt=2, member_cnt=2,
                              link=''),
                    ]
                }
            }
        }
        workflow_output = {}
        p = TransformFocusesResultProcessor()
        p.run(workflow_input, {}, workflow_output)
        print(json.dumps(workflow_output['result'], ensure_ascii=False, indent=2))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
