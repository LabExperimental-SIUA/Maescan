from abc import ABCMeta, abstractmethod


class Task(metaclass=ABCMeta):

    @abstractmethod
    def exec(self, params):
        pass
