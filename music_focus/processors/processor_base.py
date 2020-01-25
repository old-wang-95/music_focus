import abc


class ProcessorBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self, workflow_input, workflow_output):
        pass
