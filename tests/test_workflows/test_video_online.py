import json
import unittest

from music_focus.workflows.video_online import VideoOnline


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        workflow_input = {
            'result_type': 'videos'
        }
        wf = VideoOnline()
        r = wf.run(workflow_input)
        print(json.dumps(r, ensure_ascii=False, indent=2))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
