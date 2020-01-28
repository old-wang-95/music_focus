import abc


class ServerBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def start(self):
        pass
