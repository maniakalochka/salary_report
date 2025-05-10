from abc import ABC, abstractmethod


class OutputFormat(ABC):

    @abstractmethod
    def save(self, data: dict, filepath: str) -> None:
        raise NotImplementedError("Subclasses must implement this method")
