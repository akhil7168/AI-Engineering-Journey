from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for every AI tool.
    """

    name = ""
    description = ""

    @abstractmethod
    def execute(self, **kwargs):
        """
        Execute the tool.
        """
        pass

    def info(self):
        """
        Tool metadata.
        """

        return {
            "name": self.name,
            "description": self.description
        }