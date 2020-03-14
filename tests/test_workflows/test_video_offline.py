import unittest

from music_focus.workflows.video_offline import VideoOffline


class MyTestCase(unittest.TestCase):
    def test_something(self):
        workflow_input = {'result_type': 'videos'}
        wf = VideoOffline()
        r = wf.run(workflow_input)
        print(r)


if __name__ == '__main__':
    unittest.main()
