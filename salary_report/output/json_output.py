import json

from .base import OutputFormat


class JSONOutput(OutputFormat):
    def save(self, data: dict, filepath: str) -> None:
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
