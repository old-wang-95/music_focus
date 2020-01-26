import unittest

from music_focus.workflows.weibo_offline import WeiboOffline


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        workflow_input = {}
        wf = WeiboOffline()
        r = wf.run(workflow_input)
        print(r)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
