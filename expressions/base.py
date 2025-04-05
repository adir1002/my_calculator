from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def evaluate(self, context):
        pass
