from abc import ABC, abstractmethod


class BaseReport(ABC):

    @abstractmethod
    def generate(self, data):
        raise NotImplementedError("Subclasses must implement this method")
