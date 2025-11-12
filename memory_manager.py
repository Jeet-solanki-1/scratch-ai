#TODO business logic over repository
# memory_manager.py
from typing import Dict, Optional
from memory_repository import MemoryRepository

class MemoryManager:
    """
    Business logic around memory operations:
    - get_fact
    - set_fact
    - delete_fact
    - list_facts
    Keeps an in-memory cache and delegates persistence to MemoryRepository.
    """

    def __init__(self, repository: MemoryRepository):
        self.repository = repository
        pass

    def load(self) -> None:
        """Load facts from repository into local cache."""
        pass

    def get_fact(self, key: str) -> Optional[str]:
        """Return value for key or None."""
        pass

    def set_fact(self, key: str, value: str) -> None:
        """Set and persist a fact."""
        pass

    def delete_fact(self, key: str) -> bool:
        """Delete a fact; return True if deleted, False if not found."""
        pass

    def list_facts(self) -> Dict[str, str]:
        """Return a shallow copy of all facts."""
        pass

    def clear(self) -> None:
        """Clear all memory and persist reset state."""
        pass
