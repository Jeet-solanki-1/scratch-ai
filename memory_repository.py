 #TODO persistence interface

from typing import Dict, Optional

class MemoryRepository:
    """
    Repository handling persisitance of facts.
    Default implimentation may use JSON file.
    """
    def __init__(self,path:str="memory.json"):
        """
        Initialize repository with a file path (or other backend).
        """
        pass
    def load_all(self) -> Dict[str,str]:
        """Load all facts from persistent store; """
        pass
    def save_all(self,facts: Dict[str,str]) -> None:
        """Persists the entire facts dictionary automatically."""
        pass
    def exists(self,key: str) -> bool:
        """Return true if key exists in persistent store (can be in-memory cache)."""
        pass


    
