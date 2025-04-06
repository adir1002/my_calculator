from abc import ABC, abstractmethod

class Expression(ABC):

    @abstractmethod
    def __init__(self,*args):
        pass

    @abstractmethod
    def evaluate(self, context):
        pass

    @staticmethod
    @abstractmethod
    def is_valid(*args):
        pass
