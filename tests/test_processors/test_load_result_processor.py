import unittest

from music_focus.processors.load_result_processor import LoadResultProcessor


class Test(unittest.TestCase):

    def setUp(self):
        self.data_dir = 'tests/data'

    def test_load_posts(self):
        print('test_load_posts~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        workflow_input = {
            'result_type': 'posts'
        }
        p = LoadResultProcessor(self.data_dir)
        p.run(workflow_input, {}, {})
        p.run(workflow_input, {}, {})
        print(workflow_input['posts'])

    def test_load_focuses(self):
        print('test_load_focuses~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        workflow_input = {
            'result_type': 'focuses'
        }
        p = LoadResultProcessor(self.data_dir)
        p.run(workflow_input, {}, {})
        p.run(workflow_input, {}, {})
        print(workflow_input['focuses'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
