import pickle
from datetime import datetime

from music_focus.processors.processor_base import ProcessorBase


class SaveResultProcessor(ProcessorBase):

    def __init__(self, data_dir='./data'):
        self._data_dir = data_dir

    def run(self, workflow_input, tmp_result, workflow_output):
        result = {
            'scores': tmp_result['scores']
        }
        if 'posts' in tmp_result:
            result['posts'] = tmp_result['posts']
        elif 'focuses' in tmp_result:
            result['focuses'] = tmp_result['focuses']
        file_name = datetime.now().strftime('result_%Y-%m-%d_%H:%M:%S.pkl')
        with open('{}/{}'.format(self._data_dir, file_name)) as f:
            pickle.dump(result, f)
