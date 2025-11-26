from abc import ABC, abstractmethod

class BaseMemory(ABC):
    """
    Abstract base class for agent memory.
    """
    
    @abstractmethod
    def add(self, key: str, value: str):
        """Stores a value in memory."""
        pass

    @abstractmethod
    def get(self, key: str) -> str:
        """Retrieves a value from memory."""
        pass

    @abstractmethod
    def clear(self):
        """Clears the memory."""
        pass
