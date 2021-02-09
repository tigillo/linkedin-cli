from abc import ABCMeta, abstractmethod


class BaseCommand(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, args):
        pass
