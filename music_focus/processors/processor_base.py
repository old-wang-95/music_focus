import abc


class ProcessorBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self, workflow_input, tmp_result, workflow_output):
        pass
