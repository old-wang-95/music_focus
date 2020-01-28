import pickle
from datetime import datetime

from music_focus.processors.processor_base import ProcessorBase


class SaveResultProcessor(ProcessorBase):

    def __init__(self, data_dir='./data'):
        self._data_dir = data_dir

    def run(self, workflow_input, tmp_result, workflow_output):
        rtype = workflow_input['result_type']
        result = {
            'scores': tmp_result['scores'],
            rtype: tmp_result[rtype]
        }
        file_name = datetime.now().strftime('{}_%Y-%m-%d_%H:%M:%S.pkl'.format(rtype))
        with open('{}/{}'.format(self._data_dir, file_name), 'wb') as f:
            pickle.dump(result, f)
        workflow_output['result'] = file_name
