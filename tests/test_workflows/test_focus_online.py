import unittest
import json

from music_focus.workflows.focus_online import FocusOnline


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        workflow_input = {'result_type': 'focuses'}
        wf = FocusOnline()
        r = wf.run(workflow_input)
        print(json.dumps(r, ensure_ascii=False, indent=2))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
