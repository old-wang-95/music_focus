import unittest

from music_focus.workflows.focus_offline import FocusOffline


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        workflow_input = {'result_type': 'focuses'}
        wf = FocusOffline()
        r = wf.run(workflow_input)
        print(r)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
