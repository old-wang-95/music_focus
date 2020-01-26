import os
import pickle
from datetime import datetime

from music_focus.processors.processor_base import ProcessorBase


class LoadResultProcessor(ProcessorBase):

    def __init__(self, data_dir='./data'):
        self._data_dir = data_dir

    def run(self, workflow_input, tmp_result, workflow_output):
        rtype = workflow_input['result_type']
        if rtype not in workflow_input:
            # 没加载过, 加载
            result_file_name = self._find_newest_result_file(self._data_dir, rtype,
                                                             '{}_%Y-%m-%d_%H:%M:%S.pkl'.format(rtype))
            workflow_input[rtype] = self._load_result(self._data_dir, result_file_name)
        else:
            # 加载过, 根据是否版本最新进行重载
            result_file_name = self._find_newest_result_file(self._data_dir, rtype,
                                                             '{}_%Y-%m-%d_%H:%M:%S.pkl'.format(rtype))
            if result_file_name != workflow_input[rtype]['file_name']:
                workflow_input[rtype] = self._load_result(self._data_dir, result_file_name)

    @staticmethod
    def _find_newest_result_file(dir_name, rtype, file_formatter):
        return max([f for f in os.listdir(dir_name) if rtype in f],
                   key=lambda f: datetime.strptime(f, file_formatter))

    @staticmethod
    def _load_result(data_dir, result_file_name):
        with open('{}/{}'.format(data_dir, result_file_name), 'rb') as f:
            result = pickle.load(f)
        result['file_name'] = result_file_name
        return result
