import abc

from music_focus import logger


class WorkflowBase(metaclass=abc.ABCMeta):

    def __init__(self):
        self._processors = []

    @abc.abstractmethod
    def load_processors(self):
        pass

    def run(self, workflow_input):
        assert len(self._processors) > 0, 'no processor be loaded!'
        workflow_output = {}
        for processor in self._processors:
            logger.info('start to run processor: {}'.format(processor.__name__))
            processor.run(workflow_input, workflow_output)
            logger.info('processor: {} run finish'.format(processor.__name__))
        assert 'result' in workflow_output, 'can not find result in workflow_output!'
        return workflow_output['result']
